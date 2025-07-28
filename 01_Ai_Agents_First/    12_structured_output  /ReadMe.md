
Output Types: Structured Output with Pydantic

Structured outputs are crucial when you need your AI agents to provide data in a predictable and usable format. Instead of free-form text, you can enforce a specific structure, making it easier for your applications to parse and utilize the information. The OpenAI Agents SDK provides mechanisms to achieve this.

Why Use Structured Outputs?

Data Parsing: Easier to extract specific information without complex text parsing.

Integration: Seamless integration with other systems that expect structured data (e.g., databases, APIs).

Reliability: Reduces ambiguity and ensures consistent data formatting.

Automation: Automate workflows that rely on specific data points.

Structured Outputs vs. JSON Mode:

It's important to differentiate between "Structured Outputs" and the simpler "JSON mode." "JSON mode" ensures that the output is valid JSON, but it doesn't guarantee that it conforms to a specific schema. "Structured Outputs" goes further, guaranteeing schema adherence. This is a very important distinction.


Make your Notebook capable of running asynchronous functions.

Both Jupyter notebooks and Python’s asyncio library utilize event loops, but they serve different purposes and can sometimes interfere with each other.

The nest_asyncio library allows the existing event loop to accept nested event loops, enabling asyncio code to run within environments that already have an event loop, such as Jupyter notebooks.

In summary, both Jupyter notebooks and Python’s asyncio library utilize event loops to manage asynchronous operations. When working within Jupyter notebooks, it’s essential to be aware of the existing event loop to effectively run asyncio code without conflicts.
