from livekit.plugins import openai

from ....configs.app_config import Talk2MeConfig


class OpenAILargeLanguageModel:
    """
    Model class for OpenAI large language model.
    """

    def invoke(self, config: Talk2MeConfig):
        return openai.LLM(model=config.openai.OPENAI_MODEL)
