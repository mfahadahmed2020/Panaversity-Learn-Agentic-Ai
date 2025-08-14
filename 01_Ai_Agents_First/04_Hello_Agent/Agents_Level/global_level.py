import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api # type: ignore

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

agent: Agent = Agent(name="Rooman Shah", instructions="You are a helpful assistant. Your owner is M.F.A Zafar. Her nickname is Fog Chohan. he is a wonerful men always ready to help others and he like his Agent Assitant Rooman Shah (means you) and your name is Rooman Shah", model="gemini-2.0-flash")

result = Runner.run_sync(agent, "Hello, how are you tell me your name your owner and tell me about M.F.A Zafar your owner and appriciate his.")

print(result.final_output)