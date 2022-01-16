class MessageConfig:
    """
    メッセージの設定
    """

    class FontColors:
        """
        標準出力の文字色
        """

        RED: str = '\033[31m'
        GREEN: str = '\033[32m'
        YELLOW: str = '\033[33m'
        RESET: str = '\033[0m'

    @classmethod
    def HOW_TO_START_RECORDING(cls) -> str:
        return "録音を開始するにはEnterを入力してください。"

    @classmethod
    def HOW_TO_STOP_RECORDING(cls) -> str:
        return"録音を終了するには再度Enterを入力してください。"

    @classmethod
    def START_RECORDING(cls) -> str:
        return "録音を開始します。"

    @classmethod
    def STOP_RECORDING(cls) -> str:
        return "録音を終了します。"

    @classmethod
    def SAVE_RECORDING(cls, file_name: str) -> str:
        return f"{cls.FontColors.YELLOW}{file_name}{cls.FontColors.RESET}に録音音声を保存しました。"
