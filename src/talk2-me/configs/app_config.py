import os

from dotenv import load_dotenv

from configs.service.deepgram import DeepgramConfig
from configs.service.livekit import LivekitConfig
from configs.service.openai import OpenAIConfig

load_dotenv()


class Talk2MeConfig:
    openai = OpenAIConfig(
        OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY") or '',
        OPENAI_MODEL=os.environ.get("OPENAI_MODEL") or '',
    )
    livekit = LivekitConfig(
        LIVEKIT_URL=os.environ.get("LIVEKIT_URL") or '',
        LIVEKIT_API_KEY=os.environ.get("LIVEKIT_API_KEY") or '',
        LIVEKIT_API_SECRET=os.environ.get("LIVEKIT_API_SECRET") or '',
    )
    deepgram = DeepgramConfig(
        DEEPGRAM_API_KEY=os.environ.get("DEEPGRAM_API_KEY") or '',
    )
