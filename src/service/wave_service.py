import pyaudio
import threading

from config.wave_config import WaveConfig
from config.message_config import MessageConfig
from model.wave_model import WaveModel
from repository.wave_repository import WaveRepository


class WaveService:
    """
    音声サービス
    """

    wave_repository: WaveRepository
    """
    音声リポジトリ
    """

    pyaudio_stream: pyaudio.Stream
    """
    ストリーミング音声処理機
    """

    def __init__(self, wave_repository: WaveRepository):
        self.wave_repository = wave_repository

        # pyaudioのセットアップ
        self.stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=WaveConfig.CHANNELS,
            rate=WaveConfig.RATE,
            input=True,
            output=False,
            frames_per_buffer=WaveConfig.CHUNK,
        )

    def record_wave(self):
        """
        音声を録音する
        Enterを入力すると録音開始、再入力すると終了
        """

        # 録音状態を切り替えるためのフラグ
        start_recording: bool = False
        stop_recording: bool = False

        wave_chunks: list[bytes] = []

        def async_record_wave():
            """
            非同期でストリーミングするための関数
            threading経由で呼び出す
            """

            # 録音開始されるまで待機
            while not start_recording:
                pass

            # 録音終了されるまで録音
            while not stop_recording:
                chunk = self.stream.read(WaveConfig.CHUNK, exception_on_overflow=False)
                wave_chunks.append(chunk)

        # 非同期でストリーミング
        thread: threading.Thread = threading.Thread(target=async_record_wave)
        thread.start()

        # TODO: Spaceキーを押すと録音開始、離すと終了
        print(MessageConfig.HOW_TO_START_RECORDING())
        input()
        start_recording = True

        print(MessageConfig.HOW_TO_STOP_RECORDING())
        input()
        stop_recording = True

        # 音声を保存
        wave_model: WaveModel = WaveModel(
            content=b''.join(wave_chunks),
            length=len(wave_chunks) * WaveConfig.CHUNK / WaveConfig.RATE
        )
        file_name: str = self.wave_repository.save(wave_model)
        print(MessageConfig.SAVE_RECORDING(file_name))

    def clear_all_data(self):
        """
        音声データを全削除する
        dataディレクトリを空にする
        """

        self.wave_repository.delete_all()
        print(MessageConfig.CLEAR_ALL_DATA())
