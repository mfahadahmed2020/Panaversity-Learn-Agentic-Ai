from agents import Agent, Runner, handoff
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

custom_refund_handoff = handoff(
    agent=refund_agent,
    tool_name_override="Custom_Refund_Tool",
    tool_description_override="Handle User Refund Requests With Extra Care."
)

damage_refund_handoff = handoff(
    agent=refund_agent,
    tool_name_override="Damage_Refund_Tool",
    tool_description_override="Handle Refund Due To Damaged Item."
)

late_delivery_refund_handoff = handoff(
    agent=refund_agent,
    tool_name_override="Late_Delivery_Refund_Tool",
    tool_description_override="Handle Refund Due To Late Delivery."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Aap User Ke Request Parhen Or Decide Karen Kay Kis Agent Ko Yeh Work Dena Hai.",
    handoffs=[billing_agent, custom_refund_handoff,
              damage_refund_handoff, late_delivery_refund_handoff]
)

async def main():
    result = await Runner.run(triage_agent,
                              "My Product Arrived Broken. I Want A Refund.'\n"
                              "My Order Was Arrived 10 Days Late. I Want A Refund.",
                              run_config=config)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())