from agents import Agent, Runner, function_tool, RunContextWrapper
import asyncio
from connection import config
from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    uid: int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"User {wrapper.context.name} is 42 Years Old."

async def main():
    user_info = UserInfo(name="M Fahad Ahmed", uid=449787)

    agent = Agent[UserInfo](
        name="Assistant",
        instructions="Use Fetch_User_Age Tool And Always Only Say Exactly What The Tool Returns.",
        tools=[fetch_user_age]
    )

    result = await Runner.run(
        starting_agent=agent,
        input="Who is The Age of The User?",
        context=user_info,
        run_config=config
    )
    
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())