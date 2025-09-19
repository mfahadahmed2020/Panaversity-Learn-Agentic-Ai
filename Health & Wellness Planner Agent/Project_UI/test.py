from health_wellness_agent.agent import HealthWellnessAgent
import asyncio

agent = HealthWellnessAgent()

async def test():
    result = await agent.handle_user("Lose 5kg", {})
    return result

if __name__ == "__main__":
    output = asyncio.run(test())
    print(output)