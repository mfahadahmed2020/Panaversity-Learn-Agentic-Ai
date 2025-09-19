import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionModel, AsyncOpenAI
from agents import enable_verbose_stdout_logging
from agents.run import RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY Not Found, Please Check Your .env File.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model= OpenAIChatCompletionModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

Health_Agent = Agent(
    name = "Smart Health Agent",
    instructions =""" You Are Smart, Health Agent Assistant.
    When A User Share A Problem (e.g., "Fahad Is Having A HeadAche".) Follow This Structure:
    
    Response Calmly & Positively. No Negative Comments.
    Suggest A HelpFul Product (e.g.,Medicine).
    Andy Additional Home Remedie.
    Also BreFly Explain Why This Medicine & Remides Helps.
    
    Tone: Caring & Clean. If You Want Make It A Little It Supportive.
"""
)

user_input = input("Enter The Problem You Are facing: ")
result = Runner.run_sync(
    Health_Agent,
    user_input,
    run_config=config
)

print(f"\nAgent's Respond On Your Query:\n")
print(f"{result.final_output}\n")