from pydantic import BaseModel, Field
from config.wave_config import WaveConfig


class WaveModel(BaseModel):
    """
    音声モデル
    """

    rate: int = Field(default=WaveConfig.RATE)
    """
    サンプリングレート[Hz]
    """

    length: float
    """
    音声の長さ[s]
    """

    content: bytes
    """
    音声データ
    """
