from config.message_config import MessageConfig
from repository.wave_repository import WaveRepository


class WaveService:
    """
    音声サービス
    """

    wave_repository: WaveRepository
    """
    音声リポジトリ
    """

    def __init__(self, wave_repository: WaveRepository):
        self.wave_repository = wave_repository

    def record_wave(self):
        """
        音声を録音する
        Enterを入力すると録音開始、再入力すると終了
        """

        # TODO: Spaceキーを押すと録音開始、離すと終了
        print(MessageConfig.HOW_TO_START_RECORDING())
        input()

        print(MessageConfig.HOW_TO_STOP_RECORDING())
        input()

        print(MessageConfig.SAVE_RECORDING("test.wav"))

    def clear_all_data(self):
        """
        音声データを全削除する
        dataディレクトリを空にする
        """

        self.wave_repository.delete_all()
        print(MessageConfig.CLEAR_ALL_DATA())
