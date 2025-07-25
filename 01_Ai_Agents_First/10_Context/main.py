from agents import Agent, Runner
from connection import config
import asyncio

# Sirf LLM Context: Instructions De Rahe Hain Agent ko
agent = Agent(
    name="PoliteAssistant",
    instructions="User Ka Name M Fahad Ahmed Hai. Hamesha Polite Raho Aur Har Jawab Main 'M Fahad Ahmed' Ka Istemaal Karo. Agar User Ka Sawal Aapko Samajh Nahi Aata Toh 'M Fahad Ahmed, Mujhe Samajh Nahi Aaya' Keh Kar Bulao.",
)

async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Who is The President of Pakistan?",
        run_config=config # Ye Bhi LLM Context Hai
    )
    
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())


