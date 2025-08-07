Agent Loop



Agent Loop Agent Loop
LifeCycle

In general terms, a lifecycle refers to the complete sequence of stages that an object, process, or entity goes through from its creation to its termination.

In the context of the OpenAI Agents SDK, it specifically describes the stages an agent experiences—from when it’s initialized (or activated) until it completes its task and produces an output.
Lifecycle events (hooks)

Sometimes, you want to observe the lifecycle of an agent. For example, you may want to log events, or pre-fetch data when certain events occur. You can hook into the agent lifecycle with the hooks property. Subclass the AgentHooks class, and override the methods you're interested in.

In the OpenAI Agents SDK, lifecycle management is provided at two levels:

    Run-Level Lifecycle (RunHooks):
    This manages global events that span the entire execution or "run" of one or more agents. It allows you to monitor and control overarching events such as the start and end of an agent's execution, tool invocations, and handoffs between agents.

    Agent-Level Lifecycle (AgentHooks):
    This focuses on the individual agent. It lets you inject custom logic right into the agent's specific workflow—tracking events such as when an agent starts processing, when it completes its task, and when it interacts with external tools.

These two layers allow for both a broad view of the system's execution (through RunHooks) and a detailed, fine-grained control of each agent's behavior (via AgentHooks).
Run LifeCycle in the OpenAI Agents SDK

In the SDK, the run lifecycle is managed through RunHooks. These hooks allow you to observe and control events that occur across the entire run of one or more agents. They include callbacks for when an agent starts or ends, when a tool is about to run, and when control is handed off between agents. You can add callbacks on these (lifecycle events)[https://openai.github.io/openai-agents-python/ref/lifecycle/#agents.lifecycle.RunHooks] in an agent run:

    on_agent_start async: Called before the agent is invoked. Called each time the current agent changes.
    on_agent_end async: Called when the agent produces a final output.
    on_handoff async: Called when a handoff occurs.
    on_tool_start async: Called before a tool is invoked.
    on_tool_end async: Called after a tool is invoked.


Learning References

    https://openai.github.io/openai-agents-python/agents/#lifecycle-events-hooks
    https://openai.github.io/openai-agents-python/ref/run/#agents.run.Runner
    https://openai.github.io/openai-agents-python/ref/lifecycle/#agents.lifecycle.RunHooks
    https://openai.github.io/openai-agents-python/ref/lifecycle/#agents.lifecycle.AgentHooks
