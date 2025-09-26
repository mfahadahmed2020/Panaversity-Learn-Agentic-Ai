from agents import Agent, Runner, function_tool
from connection import config
import os
from dotenv import load_dotenv
import requests

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")


@function_tool
def get_weather(city: str) -> str:
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"),
    data = response.json()
    return (f"The Current Weather In {city} Is {data['current']['temp_c']}°C With {data['current']['condition']['text']}.")

agent = Agent(
    name = 'Weather Agent',
    instructions="You Are A Helpful Assistant. Your Task Is To Help The User With Their Queries.",
    tools=[get_weather]
)

result = Runner.run_sync(agent,
                         "What Is The Current Weather In Karachi Today?",
                         run_config=config)

print(result.final_output)