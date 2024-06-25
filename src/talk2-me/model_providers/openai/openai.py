import livekit.agents as a

from .llm.llm import OpenAILargeLanguageModel
from .speech2text.speech2text import OpenAISpeech2TextModel
from .tts.tts import OpenAIText2SpeechModel


class OpenAIProvider:
    def __init__(
        self,
    ) -> None:
        pass

    @property
    def llm():
        return OpenAILargeLanguageModel()

    @property
    def tts():
        return OpenAIText2SpeechModel()

    @property
    def stt():
        return OpenAISpeech2TextModel()
