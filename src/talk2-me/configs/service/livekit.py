from pydantic import BaseModel, Field


class LivekitConfig(BaseModel):
    """
    Livekit service config
    """

    LIVEKIT_URL: str = Field(
        description="",
        default=None,
    )
    LIVEKIT_API_KEY: str = Field(
        description="",
        default=None,
    )
    LIVEKIT_API_SECRET: str = Field(
        description="",
        default=None,
    )
