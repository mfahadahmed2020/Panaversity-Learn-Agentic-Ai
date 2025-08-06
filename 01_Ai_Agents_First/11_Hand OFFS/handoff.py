from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    RunConfig,
    handoff
    )
from openai import AsyncOpenAI
import rich

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
    tracing_disabled=False
    )

next_js_assistant =Agent(name="Next js Assistant")
python_assistant = Agent(name="Python Assistant")
python_handoff = handoff(
    agent=python_assistant,
    tool_name_override="specialized_python_agent",
    tool_description_override="you are speclized python agent")

lead_agent = Agent(
    name="Lead Agent", 
    instructions="You are Lead agent you will be given task and you have to handoff to the specialized agents accordingly",
    handoffs=[
        next_js_assistant,
        python_handoff
        ]
)

result  = Runner.run_sync(
    starting_agent=lead_agent,
    input="I am having some issue with python decorators",
    run_config=config
    )

print("last Agent>>>>>",result.last_agent)   
rich.print("result>>>>", result.final_output)