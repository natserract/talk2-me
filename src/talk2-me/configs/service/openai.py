from pydantic import BaseModel, Field


class OpenAIConfig(BaseModel):
    """
    OpenAI service config
    """

    OPENAI_API_KEY: str = Field(
        description="",
        default=None,
    )
