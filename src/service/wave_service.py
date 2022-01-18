import pyaudio
import threading
import numpy as np

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

        wave_content: list[int] = []

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
                wave_content.extend(np.frombuffer(chunk, dtype=np.int16))

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
            content=wave_content,
            length=len(wave_content) / WaveConfig.RATE
        )
        file_name: str = self.wave_repository.save(wave_model)
        print(MessageConfig.SAVE_WAVE_FILE(file_name))

    def clear_all_data(self):
        """
        音声データを全削除する
        dataディレクトリを空にする
        """

        self.wave_repository.delete_all()
        print(MessageConfig.CLEAR_ALL_DATA())

    def steganography(self):
        """
        音声データに電子透かしを埋め込む

        下記ブログを参考にLSB置換法で実装
        https://tam5917.hatenablog.com/entry/2020/02/07/000644
        """

        # ファイル一覧を表示
        print(MessageConfig.SELECT_WAVE_FILE_TO_STEGANOGRAPHY())
        wave_models = self.wave_repository.get_all()
        for i, wave_model in enumerate(wave_models):
            print(MessageConfig.WAVE_FILE_WITH_INDEX(i, wave_model.file_name))

        # ユーザが音声とメッセージを指定する
        try:
            print("")
            print(MessageConfig.INPUT_WAVE_FILE_INDEX(0, len(wave_models) - 1), end="")
            wave_model_index: int = int(input())
            # インデックスが範囲を超えている場合はエラー
            if (wave_model_index not in range(len(wave_models))):
                raise Exception
            wave_model: WaveModel = wave_models[wave_model_index]

            print(MessageConfig.INPUT_MESSAGE(), end="")
            message: str = input()
            # メッセージが空の場合はエラー
            if (message == ""):
                raise Exception
        except Exception:
            print(MessageConfig.VALIDATION_ERROR_OF_INPUT_TEXT())
            exit(1)

        print("")
        print(MessageConfig.START_STEGANOGRAPHY())

        # メッセージを"{文字数}:{メッセージ}"に加工する
        # 文字数が不明だと検出できないため
        message = f"{len(message)}:{message}"
        # ビット列に変換 (ex. "test" -> "01110100011001010111001101110100")
        message_bits: str = "".join([format(ord(ch), "#010b") for ch in message]).replace("0b", "")

        # LSB置換法で最下位ビットにメッセージを埋め込む
        for i, bit in enumerate(message_bits):
            wave_model.content[i] = wave_model.content[i] & ~1 | int(bit)

        print(MessageConfig.COMPLETE_STEGANOGRAPHY())

        # ファイルを保存
        file_name: str = self.wave_repository.save(wave_model)
        print("")
        print(MessageConfig.SAVE_WAVE_FILE(file_name))
