from agent import Agent, Runner, RunConfig
from agents.models.openai_provider import AsyncAI, OpenAIChatCompletionsModel

GEMINI_API_KEY = "AIzaSyAyDm4CYXIUlmiXfDgNVbOZOlF7Il71ehw"

# Provider Using Gemini's OpenAI - Compatible EndPoint
provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beata/openai",
    api_key=GEMINI_API_KEY,
)

# Gemini Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# Runner Config
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

# Define The Agent Properly (Instantiate IT!)
agent = Agent(
    name="Hello World",
    instruction="You Are A HelpFul Agent For Answerig Every Question!",
)

# Run Synchronously
result = Runner.run(agent, "Write A Haiku About Recursion In Programming", run_config=run_config)

print(result.final_output)