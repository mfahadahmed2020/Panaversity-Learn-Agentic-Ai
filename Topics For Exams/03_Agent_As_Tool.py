from agents import Agent, Runner
from connection import config

# Define Individual Translator Agents

italian_agent = Agent(
    name ="Italian Translator",
    instructions="Translate Any English Text into Italian.",
)

spanish_agent = Agent(
    name ="Spanish Translator",
    instructions="Translate Any English Text into Spanish.",
)

french_agent = Agent(
    name ="French Translator",
    instructions="Translate Any English Text into French.",
)

urdu_agent = Agent(
    name ="Urdu Translator",
    instructions="Translate Any English Text into Urdu.",
)

# Define Main Agent That Routes to The Right Translator

translation_router = Agent(
    name="Translation Router",
    instructions=""""
    You Are a Translation Assistant. Route The Translation Request to The Correct Language Agent.
    Use The Appropriate Tool to Convert English Text into Either Italian, Spanish, French, or
    Urdu Based On The Request.
    """,
    tools=[
        # Convert These Agents InTo Tools
        italian_agent.as_tool(
            tool_name="Translate_To_Italian",
            tool_description="Translate The User's Message To Italian."
        ),
        spanish_agent.as_tool(
            tool_name="Translate_To_Spanish",
            tool_description="Translate The User's Message To Spanish."
        ),
        french_agent.as_tool(
            tool_name="Translate_To_french",
            tool_description="Translate The User's Message To French."
        ),
        urdu_agent.as_tool(
            tool_name="Translate_To_Urdu",
            tool_description="Translate The User's Message To Urdu."
        )
    ]
)
    
# Example Input
result = Runner.run_sync(urdu_agent, "Translate I Love Learning into Urdu.", run_config=config)

print(result.final_output)