import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled  # type: ignore
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

model : OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

async def main():
    agent = Agent(
        name="M Fahad Ahmed Assistant",
        instructions="You only respond like a friend and with some detailed answer. Your owner or boss is M.A Zafar and her nickname is Syed , and your name is Zaid Khan Afandi",
        model=model,
    )
    
    result = await Runner.run(
        agent,
        "Tell me about your name and tell the meaning or Fahad, Syed and Zaid"
    )
    print()
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())    