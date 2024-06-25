import os

from dotenv import load_dotenv

from .service.deepgram import DeepgramConfig
from .service.livekit import LivekitConfig
from .service.openai import OpenAIConfig

load_dotenv()


class Talk2MeConfig:
    openai = OpenAIConfig(OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY"))
    livekit = LivekitConfig(
        LIVEKIT_URL=os.environ.get("LIVEKIT_URL"),
        LIVEKIT_API_KEY=os.environ.get("LIVEKIT_API_KEY"),
        LIVEKIT_API_SECRET=os.environ.get("LIVEKIT_API_SECRET"),
    )
    deepgram = DeepgramConfig(
        DEEPGRAM_API_KEY=os.environ.get("DEEPGRAM_API_KEY"),
    )
