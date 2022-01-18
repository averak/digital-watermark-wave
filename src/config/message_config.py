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
    def SAVE_WAVE_FILE(cls, file_name: str) -> str:
        return f"{cls.FontColors.YELLOW}{file_name}{cls.FontColors.RESET}に音声データを保存しました。"

    @classmethod
    def CLEAR_ALL_DATA(cls) -> str:
        return f"{cls.FontColors.GREEN}音声データを全削除しました。{cls.FontColors.RESET}"

    @classmethod
    def INPUT_MESSAGE(cls) -> str:
        return "メッセージを入力: "

    @classmethod
    def INPUT_WAVE_FILE_INDEX(cls, start: int, end: int) -> str:
        return f"ファイルを選択 ({start}-{end}): "

    @classmethod
    def WAVE_FILE_WITH_INDEX(cls, index: int, file_name: str) -> str:
        return f"{index}: {cls.FontColors.YELLOW}{file_name}{cls.FontColors.RESET}"

    @classmethod
    def SELECT_WAVE_FILE_TO_STEGANOGRAPHY(cls) -> str:
        return "電子透かしを埋め込むファイルを選択してください。"

    @classmethod
    def VALIDATION_ERROR_OF_INPUT_TEXT(cls) -> str:
        return f"{cls.FontColors.RED}無効な値が入力されました。{cls.FontColors.RESET}"

    @classmethod
    def START_STEGANOGRAPHY(cls) -> str:
        return "処理を開始します。"

    @classmethod
    def COMPLETE_STEGANOGRAPHY(cls) -> str:
        return "処理が完了しました。"
