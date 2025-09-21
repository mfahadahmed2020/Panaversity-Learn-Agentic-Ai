from agents import Agent, Runner, function_tool
from config import config

@function_tool
def usd_to_pkr():
    return 'Today USD to PKR is Current Rate 280.'

agent = Agent(
    name = 'General Agent',
    instructions="You Are A Helpful Assistant. Your Task Is To Help The User With Their Queries.",
    tools=[usd_to_pkr]
)

result = Runner.run_sync(agent,
                         "What Is USD To PKR Today's?",
                         run_config=config)

print(result.final_output)