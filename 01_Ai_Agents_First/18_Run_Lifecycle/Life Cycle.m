Lifecycle

RunHooks module-attribute

RunHooks = RunHooksBase[TContext, Agent]

Run hooks when using Agent.
AgentHooks module-attribute

AgentHooks = AgentHooksBase[TContext, Agent]

Agent hooks for Agents.
RunHooksBase

Bases: Generic[TContext, TAgent]

A class that receives callbacks on various lifecycle events in an agent run. Subclass and override the methods you need.
on_agent_start async

on_agent_start(
    context: RunContextWrapper[TContext], agent: TAgent
) -> None

Called before the agent is invoked. Called each time the current agent changes.
on_agent_end async

on_agent_end(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    output: Any,
) -> None

Called when the agent produces a final output.
on_handoff async

on_handoff(
    context: RunContextWrapper[TContext],
    from_agent: TAgent,
    to_agent: TAgent,
) -> None

Called when a handoff occurs.
on_tool_start async

on_tool_start(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    tool: Tool,
) -> None

Called before a tool is invoked.
on_tool_end async

on_tool_end(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    tool: Tool,
    result: str,
) -> None

Called after a tool is invoked.
AgentHooksBase

Bases: Generic[TContext, TAgent]

A class that receives callbacks on various lifecycle events for a specific agent. You can set this on agent.hooks to receive events for that specific agent.

Subclass and override the methods you need.
on_start async

on_start(
    context: RunContextWrapper[TContext], agent: TAgent
) -> None

Called before the agent is invoked. Called each time the running agent is changed to this agent.
on_end async

on_end(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    output: Any,
) -> None

Called when the agent produces a final output.
on_handoff async

on_handoff(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    source: TAgent,
) -> None

Called when the agent is being handed off to. The source is the agent that is handing off to this agent.
on_tool_start async

on_tool_start(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    tool: Tool,
) -> None

Called before a tool is invoked.
on_tool_end async

on_tool_end(
    context: RunContextWrapper[TContext],
    agent: TAgent,
    tool: Tool,
    result: str,
) -> None

Called after a tool is invoked.
