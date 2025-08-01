from agents import Agent, Runner
import asyncio
from connection import config

billing_agent = Agent(
    name="Billing Agent",
    instructions="Aap Sirf Billing SE Related Sawalon Ka Jawab Denge"
)

refund_agent = Agent(
    name="Refund Agent",
    instructions="Aap Sirf Refund Process Karne Main Madad Karenge."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Aap User Ke Request Parhen Or Decide Karen Kay Kis Agent Ko Yeh Work Dena Hai.",
    handoffs=[billing_agent, refund_agent]
)

async def main():
    result = await Runner.run(triage_agent,
                              "I Need A Refund For My Recent Purchase.'\n"
                              "Why Is My Bill So High?",
                              run_config=config)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())