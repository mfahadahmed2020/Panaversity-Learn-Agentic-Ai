import asyncio
from connection import config
from agents import Agent, Runner, input_guardrail, GuardrialFunctionOutput, InputGuardrailTripwireTriggered
from pydantic import BaseModel
import rich

class PassengerOutput():
    response: str
    isWeightExceed: bool

airport_security_guard = Agent(
    name="AirPort Security Guard",
    instructions="""Your Task Is To Check The Passenger Luggage.
    If Passenger's Luggage Is More Then 25Kgs, GraceFully Stop Them.""",
    output_type= PassengerOutput
)

@input_guardrail
async def security_guardrail(ctx, agent, input):

    result= await Runner.run(airport_security_guard, input, run_config=config)
    rich.print(result.final_output)

    return GuardrialFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=True
    )

passenger = Agent(
    name="Passenger",
    instructions="You Are A Passenger Agent.",
    input_guardrail=[security_guardrail]
)

async def main():
    try:
        result = await Runner.run(passenger, "My Luggage Weight Is 50KGs.", run_config=config)
        print(result)
    except InputGuardrailTripwireTriggered:
        print("Passenger CanNot Check-In")







if __name__ == "__main__":
    asyncio.run(main())