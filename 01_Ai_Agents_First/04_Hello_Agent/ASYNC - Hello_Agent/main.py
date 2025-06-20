from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import asyncio

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def main():
    agent = Agent(
        name = "Chief - X2 Translator",
        instructions = "You Are A HelpFul Translation. Always Translate Urdu to English Sentencess InTo Clear and Simple English to Urdu"
    )

    response = await Runner.run(
        agent,
        input = "My Name Is M Fahad Ahmed. I Am A Student of GIAIC./nمیرا نام ایم فہد احمد ہے۔ میں جی آئی اے آئی سی کا طالب علم ہوں۔",
        run_config = config
    )

    print(response)
asyncio.run(main())