from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load .env File & Get API KEY
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Check If Key Exits
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY Not Set.Please Ensure Defined Your .env File")

# Setup OpenRouter Client ( Like OpenAI , But Via OpenRouter )
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

# Chose Any OpenRouter-Supported Model
model = OpenAIChatCompletionsModel(
    model="opengvlab/internvl3-14b:free", # Example Model, RePlace If Needed
    openai_client=external_client
)

# Steup Config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define Agent
agent = Agent(
    name = "Chief - X2 Writer Agent",
    instructions = "You Are A Writer Agent. Generate Stories, Novels, Urdu Spy Series ETC."
)

# Input & Run Agent 
response = Runner.run_sync(
    agent,
    input = "Write A Short Story Introduction Imran Series SPY Novel In Simple Urdu & English",
    run_config = config
)

# OutPut
print(response)