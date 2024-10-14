import asyncio
import logging

from livekit.agents import JobContext, JobRequest, tokenize, tts
from livekit.agents.llm import ChatContext, ChatMessage, ChatRole
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import deepgram, openai

from configs.app_config import Talk2MeConfig
from providers.livekit.plugins import silero


class WorkflowManager:
    async def arun_workflow(self, ctx: JobContext):
        initial_ctx = ChatContext(
            messages=[
                ChatMessage(
                    role=ChatRole.SYSTEM,
                    text="You are a voice assistant created by LiveKit. Your interface with users will be voice. Pretend we're having a conversation, no special formatting or headings, just natural speech.",
                )
            ]
        )

        # Since OpenAI does not support streaming TTS, we'll use it with a StreamAdapter
        # to make it compatible with the VoiceAssistant
        openai_tts = tts.StreamAdapter(
            tts=openai.TTS(voice="alloy"),
            sentence_tokenizer=tokenize.basic.SentenceTokenizer(),
        )
        llm = openai.LLM(model=Talk2MeConfig.openai.OPENAI_MODEL)
        assistant = VoiceAssistant(
            vad=silero.VAD(),
            stt=deepgram.STT(),
            llm=llm,
            tts=openai_tts,
            chat_ctx=initial_ctx,
        )
        assistant.start(ctx.room)

        await asyncio.sleep(1)
        await assistant.say("Hey, how can I help you today?", allow_interruptions=True)

    async def request_fnc(self, req: JobRequest) -> None:
        logging.info("received request %s", req)
        await req.accept(self.arun_workflow)
