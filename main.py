import asyncio

from openai import chat
from agent import llm as agent
from google.adk.runners import InMemoryRunner
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai.types import Content, Part


runner = InMemoryRunner(agent=agent, app_name="agents")

async def _run_agent_async(user_input:str) -> str:
    session_id = "chat_session"

    try:
        await runner.session_service.create_session(
            app_name = runner.app_name,
            session_id = session_id,
            user_id = "user_1"
        )
    except Exception as e:
        pass

    content = Content(
        role = "user",
        parts=[Part(text=user_input)]
        )

    response_text= ""

    async for event in runner.run_async(
        user_id = "user_1",
        session_id = session_id,
        new_message=content
    ):
        if event.content and event.content.parts and event.author != "user":
            for part in event.content.parts:
                if part.text:
                    response_text += part.text

    return response_text


def run_agent(user_input:str) -> str:
    return asyncio.run(_run_agent_async(user_input))

