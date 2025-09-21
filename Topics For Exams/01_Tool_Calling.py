from agents import Agent, Runner
from connection import config

agent = Agent(
    name = 'General Agent',
    instructions="You Are A Helpful Assistant. Your Task Is To Help The User With Their Queries."
)

result = Runner.run_sync(agent,
                         "Who Is The Founder Of Pakistan?'\n"
                         "What Is The Conversion Rate Of USD To PKR In Today's Date?\n"
                         "What Is The Weather In Pakistani Cities?\n"
                         "What Is The ToDay Date?\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me The Top 10 Novels By Mazher Kaleem M.A?/n"
                         "Information Urdu & English To All Sentences\n",
                        run_config=config)

print(result.final_output)