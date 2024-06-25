from livekit.plugins import deepgram


class OpenAISpeech2TextModel:
    """
    Model class for OpenAI speech2text model

    We'll use Deepgram's Speech To Text (STT)
    """

    def invoke(self):
        return deepgram.STT()
