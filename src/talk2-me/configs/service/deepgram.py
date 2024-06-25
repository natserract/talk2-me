from pydantic import BaseModel, Field


class DeepgramConfig(BaseModel):
    """
    Deepgram service config
    """

    DEEPGRAM_API_KEY: str = Field(
        description="",
        default=None,
    )
