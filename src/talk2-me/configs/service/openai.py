from pydantic import BaseModel, Field


class OpenAIConfig(BaseModel):
    """
    OpenAI service config
    """

    OPENAI_API_KEY: str = Field(
        description="",
        default=None,
    )

    OPENAI_MODEL: str = Field(description="", default="gpt-3.5-turbo")
