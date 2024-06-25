import asyncio
import logging

from livekit.agents import JobContext, JobRequest
from livekit.agents.llm import ChatContext, ChatMessage, ChatRole
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import silero

from .model_providers.openai.openai import OpenAIProvider


class WorkflowManager:
    async def arun_workflow(self, ctx: JobContext):
        openai = OpenAIProvider()

        # Create an initial chat context with a system prompt
        initial_ctx = ChatContext(
            messages=[
                ChatMessage(
                    role=ChatRole.SYSTEM,
                    text="You are a voice assistant created by LiveKit. Your interface with users will be voice. Pretend we're having a conversation, no special formatting or headings, just natural speech.",
                )
            ]
        )
        assistant = VoiceAssistant(
            vad=silero.VAD(),
            stt=openai.stt.invoke(),
            llm=openai.llm.invoke(),
            tts=openai.tts.invoke(),
            chat_ctx=initial_ctx,  # Chat history context
        )

        # Start the voice assistant with the LiveKit room
        assistant.start(ctx.room)
        await asyncio.sleep(3)

        # Greets the user with an initial message
        await assistant.say("Hey, how can I help you today?", allow_interruptions=True)

    # This function is called when the worker receives a job request
    # from a LiveKit server.
    async def request_fnc(self, req: JobRequest) -> None:
        logging.info("received request %s", req)
        # Accept the job tells the LiveKit server that this worker
        # wants the job. After the LiveKit server acknowledges that job is accepted,
        # the entrypoint function is called.
        await req.accept(self.arun_workflow)
