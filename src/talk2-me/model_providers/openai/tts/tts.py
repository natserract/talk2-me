from livekit.agents import tokenize, tts
from livekit.plugins import openai


class OpenAIText2SpeechModel:
    """
    Model class for OpenAI Speech to text model.
    """

    def invoke(self):
        # Since OpenAI does not support streaming TTS, we'll use it with a StreamAdapter
        # to make it compatible with the VoiceAssistant
        openai_tts = tts.StreamAdapter(
            tts=openai.TTS(voice="alloy"),
            sentence_tokenizer=tokenize.basic.SentenceTokenizer(),
        )

        return openai_tts
