import os
import time
import glob
import wave as wave_io

from model.wave_model import WaveModel
from config.wave_config import WaveConfig


class WaveRepository:
    """
    音声リポジトリ
    """

    SAVE_PATH: str = "data"
    """
    保存するパス
    """

    def __init__(self):
        # 存在しない場合、ディレクトリを作成
        os.makedirs(self.SAVE_PATH, exist_ok=True)

    def get_all(self) -> list[WaveModel]:
        """
        全ての音声を取得

        @return 音声モデルリスト
        """

        waves: list[WaveModel] = []

        file_names: list[str] = glob.glob(f"{self.SAVE_PATH}/*.wav")
        for file_name in file_names:
            wave = self.get_by_filename(file_name)
            waves.append(wave)

        return waves

    def get_by_filename(self, file_name: str) -> WaveModel:
        """
        ファイル名から音声を取得

        @param file_name ファイル名
        @return 音声モデル
        """

        wave_read = wave_io.open(file_name, 'rb')
        wave_model = WaveModel(
            rate=wave_read.getframerate(),
            length=float(wave_read.getnframes()) / wave_read.getframerate(),
            content=wave_read.readframes(wave_read.getnframes()),
            file_name=file_name
        )
        wave_read.close()

        return wave_model

    def save(self, wave: WaveModel) -> str:
        """
        音声を保存

        @param 音声モデル
        @return 保存したファイル名
        """

        # NOTE: ファイル名を指定可能にしても良いかも
        file_name: str = self.__generate_file_name(wave)
        wave_write = wave_io.open(file_name, 'wb')
        wave_write.setframerate(wave.rate)
        wave_write.setnchannels(WaveConfig.CHANNELS)
        wave_write.setsampwidth(WaveConfig.BYTES)
        wave_write.writeframes(wave.content)
        wave_write.close()

        return file_name

    def __generate_file_name(self, wave: WaveModel) -> str:
        """
        保存するファイル名を生成

        @param 音声モデル
        @return ファイル名
        """

        # {タイムスタンプ}_{サンプリングレート[Hz]}_{音声の長さ[s]}.wav
        return "%s/%d_%d_%2.1f.wav" % (
            self.SAVE_PATH,
            int(time.time()),
            wave.rate,
            wave.length
        )

    def delete_all(self):
        """
        音声データを全削除
        """

        file_names: list[str] = glob.glob(f"{self.SAVE_PATH}/**/*.wav", recursive=True)
        for file_name in file_names:
            os.remove(file_name)
