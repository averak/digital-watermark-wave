class WaveConfig:
    """
    音声の設定
    """

    RATE: int = 16000
    """
    サンプリングレート[Hz]
    """

    CHANNELS: int = 1
    """
    音声の入力チャネル数
    """

    BYTES: int = 2
    """
    保存するバイト数
    """

    CHUNK: int = 1024
    """
    チャンク化するサンプル数
    メモリリークを防ぐために必要
    """
