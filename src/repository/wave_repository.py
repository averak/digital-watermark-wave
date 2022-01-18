import os
import time
import glob
import scipy.io.wavfile
import numpy as np

from model.wave_model import WaveModel


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

        wave_models: list[WaveModel] = []

        file_names: list[str] = glob.glob(f"{self.SAVE_PATH}/*.wav")
        for file_name in file_names:
            wave_model = self.get_by_filename(file_name)
            wave_models.append(wave_model)

        return wave_models

    def get_by_filename(self, file_name: str) -> WaveModel:
        """
        ファイル名から音声を取得

        @param file_name ファイル名
        @return 音声モデル
        """

        rate, content = scipy.io.wavfile.read(file_name)
        wave_model = WaveModel(
            rate=rate,
            length=len(content) / rate,
            content=list(content),
            file_name=file_name
        )
        return wave_model

    def save(self, wave_model: WaveModel) -> str:
        """
        音声を保存

        @param wave_model 音声モデル
        @return 保存したファイル名
        """

        # NOTE: ファイル名を指定可能にしても良いかも
        file_name: str = self.__generate_file_name(wave_model)
        scipy.io.wavfile.write(file_name, wave_model.rate, np.array(wave_model.content, dtype=np.int16))
        return file_name

    def __generate_file_name(self, wave_model: WaveModel) -> str:
        """
        保存するファイル名を生成

        @param wave 音声モデル
        @return ファイル名
        """

        # {タイムスタンプ}_{サンプリングレート[Hz]}Hz_{音声の長さ[s]}s.wav
        return "%s/%d_%dHz_%2.1fs.wav" % (
            self.SAVE_PATH,
            int(time.time()),
            wave_model.rate,
            wave_model.length
        )

    def delete_all(self):
        """
        音声データを全削除
        """

        file_names: list[str] = glob.glob(f"{self.SAVE_PATH}/**/*.wav", recursive=True)
        for file_name in file_names:
            os.remove(file_name)
