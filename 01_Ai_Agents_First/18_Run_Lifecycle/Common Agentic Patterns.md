Common agentic patterns

This folder contains examples of different common patterns for agents.
Deterministic flows

A common tactic is to break down a task into a series of smaller steps. Each task can be performed by an agent, and the output of one agent is used as input to the next. For example, if your task was to generate a story, you could break it down into the following steps:

    Generate an outline
    Generate the story
    Generate the ending

Each of these steps can be performed by an agent. The output of one agent is used as input to the next.

See the deterministic.py file for an example of this.

Handoffs and routing

In many situations, you have specialized sub-agents that handle specific tasks. You can use handoffs to route the task to the right agent.

For example, you might have a frontline agent that receives a request, and then hands off to a specialized agent based on the language of the request. See the routing.py file for an example of this.

Agents as tools

The mental model for handoffs is that the new agent "takes over". It sees the previous conversation history, and owns the conversation from that point onwards. However, this is not the only way to use agents. You can also use agents as a tool - the tool agent goes off and runs on its own, and then returns the result to the original agent.

For example, you could model the translation task above as tool calls instead: rather than handing over to the language-specific agent, you could call the agent as a tool, and then use the result in the next step. This enables things like translating multiple languages at once.

See the agents_as_tools.py file for an example of this.

LLM-as-a-judge

LLMs can often improve the quality of their output if given feedback. A common pattern is to generate a response using a model, and then use a second model to provide feedback. You can even use a small model for the initial generation and a larger model for the feedback, to optimize cost.

For example, you could use an LLM to generate an outline for a story, and then use a second LLM to evaluate the outline and provide feedback. You can then use the feedback to improve the outline, and repeat until the LLM is satisfied with the outline.

See the llm_as_a_judge.py file for an example of this.

Parallelization

Running multiple agents in parallel is a common pattern. This can be useful for both latency (e.g. if you have multiple steps that don't depend on each other) and also for other reasons e.g. generating multiple responses and picking the best one.

See the parallelization.py file for an example of this. It runs a translation agent multiple times in parallel, and then picks the best translation.

Guardrails

Related to parallelization, you often want to run input guardrails to make sure the inputs to your agents are valid. For example, if you have a customer support agent, you might want to make sure that the user isn't trying to ask for help with a math problem.

You can definitely do this without any special Agents SDK features by using parallelization, but we support a special guardrail primitive. Guardrails can have a "tripwire" - if the tripwire is triggered, the agent execution will immediately stop and a GuardrailTripwireTriggered exception will be raised.

This is really useful for latency: for example, you might have a very fast model that runs the guardrail and a slow model that runs the actual agent. You wouldn't want to wait for the slow model to finish, so guardrails let you quickly reject invalid inputs.

See the input_guardrails.py and output_guardrails.py files for examples.

عام ایجنٹ پیٹرن

یہ فولڈر ایجنٹوں کے لیے مختلف عام نمونوں کی مثالوں پر مشتمل ہے۔
تعییناتی بہاؤ

ایک عام حربہ یہ ہے کہ کسی کام کو چھوٹے مراحل کی ایک سیریز میں تقسیم کیا جائے۔ ہر کام ایک ایجنٹ کے ذریعے انجام دیا جا سکتا ہے، اور ایک ایجنٹ کا آؤٹ پٹ اگلے کے لیے بطور ان پٹ استعمال ہوتا ہے۔ مثال کے طور پر، اگر آپ کا کام کہانی بنانا تھا، تو آپ اسے درج ذیل مراحل میں تقسیم کر سکتے ہیں: 

ایک خاکہ تیار کریں۔ 
کہانی تیار کریں۔ 
اختتام پیدا کریں۔

ان اقدامات میں سے ہر ایک ایجنٹ کے ذریعہ انجام دیا جاسکتا ہے۔ ایک ایجنٹ کا آؤٹ پٹ اگلے کے ان پٹ کے طور پر استعمال ہوتا ہے۔

اس کی مثال کے لیے deterministic.py فائل دیکھیں۔

ہینڈ آف اور روٹنگ

بہت سے حالات میں، آپ کے پاس خصوصی ذیلی ایجنٹ ہوتے ہیں جو مخصوص کاموں کو سنبھالتے ہیں۔ آپ کام کو صحیح ایجنٹ تک پہنچانے کے لیے ہینڈ آف کا استعمال کر سکتے ہیں۔

مثال کے طور پر، آپ کے پاس ایک فرنٹ لائن ایجنٹ ہو سکتا ہے جو درخواست وصول کرتا ہے، اور پھر درخواست کی زبان کی بنیاد پر کسی خصوصی ایجنٹ کے حوالے کر دیتا ہے۔ اس کی مثال کے لیے routing.py فائل دیکھیں۔

ایجنٹوں کو بطور اوزار

ہینڈ آف کے لئے ذہنی ماڈل یہ ہے کہ نیا ایجنٹ "سبق سنبھالتا ہے"۔ یہ پچھلی گفتگو کی سرگزشت دیکھتا ہے، اور اس مقام سے بات چیت کا مالک ہے۔ تاہم، ایجنٹوں کو استعمال کرنے کا یہ واحد طریقہ نہیں ہے۔ آپ ایجنٹوں کو بطور ٹول بھی استعمال کر سکتے ہیں - ٹول ایجنٹ چلا جاتا ہے اور خود چلتا ہے، اور پھر نتیجہ اصل ایجنٹ کو واپس کر دیتا ہے۔

مثال کے طور پر، آپ مندرجہ بالا ترجمے کے کام کو ٹول کالز کے طور پر ماڈل بنا سکتے ہیں: زبان کے مخصوص ایجنٹ کے حوالے کرنے کے بجائے، آپ ایجنٹ کو ایک ٹول کے طور پر کال کر سکتے ہیں، اور پھر نتیجہ کو اگلے مرحلے میں استعمال کر سکتے ہیں۔ یہ ایک ساتھ متعدد زبانوں کا ترجمہ کرنے جیسی چیزوں کو قابل بناتا ہے۔

اس کی مثال کے لیے agents_as_tools.py فائل دیکھیں۔

ایل ایل ایم بطور جج

LLMs اکثر اپنے آؤٹ پٹ کے معیار کو بہتر بنا سکتے ہیں اگر فیڈ بیک دیا جائے۔ ایک عام نمونہ یہ ہے کہ ایک ماڈل کا استعمال کرتے ہوئے ردعمل پیدا کریں، اور پھر فیڈ بیک فراہم کرنے کے لیے دوسرا ماڈل استعمال کریں۔ یہاں تک کہ آپ لاگت کو بہتر بنانے کے لیے ابتدائی نسل کے لیے ایک چھوٹا ماڈل اور فیڈ بیک کے لیے ایک بڑا ماڈل استعمال کر سکتے ہیں۔

مثال کے طور پر، آپ کسی کہانی کے لیے خاکہ تیار کرنے کے لیے LLM استعمال کر سکتے ہیں، اور پھر آؤٹ لائن کا جائزہ لینے اور تاثرات فراہم کرنے کے لیے دوسرا LLM استعمال کر سکتے ہیں۔ اس کے بعد آپ آؤٹ لائن کو بہتر بنانے کے لیے فیڈ بیک کا استعمال کر سکتے ہیں، اور جب تک LLM آؤٹ لائن سے مطمئن نہیں ہو جاتا تب تک دہرائیں۔

اس کی مثال کے لیے llm_as_a_judge.py فائل دیکھیں۔

متوازی

متوازی طور پر متعدد ایجنٹوں کو چلانا ایک عام نمونہ ہے۔ یہ تاخیر دونوں کے لیے کارآمد ہو سکتا ہے (مثال کے طور پر اگر آپ کے پاس متعدد مراحل ہیں جو ایک دوسرے پر منحصر نہیں ہیں) اور دیگر وجوہات کے لیے بھی مثال کے طور پر متعدد ردعمل پیدا کرنا اور بہترین کو چننا۔

اس کی مثال کے لیے parallelization.py فائل دیکھیں۔ یہ متوازی طور پر متعدد بار ترجمہ ایجنٹ چلاتا ہے، اور پھر بہترین ترجمہ چنتا ہے۔

گارڈریلز

متوازی سے متعلق، آپ اکثر ان پٹ گارڈریلز چلانا چاہتے ہیں تاکہ یہ یقینی بنایا جا سکے کہ آپ کے ایجنٹوں کے ان پٹ درست ہیں۔ مثال کے طور پر، اگر آپ کے پاس کسٹمر سپورٹ ایجنٹ ہے، تو آپ اس بات کو یقینی بنانا چاہیں گے کہ صارف ریاضی کے مسئلے میں مدد طلب کرنے کی کوشش نہیں کر رہا ہے۔

آپ متوازی کا استعمال کرتے ہوئے کسی خاص ایجنٹ ایس ڈی کے خصوصیات کے بغیر یہ یقینی طور پر کر سکتے ہیں، لیکن ہم ایک خصوصی گارڈریل پرائمیٹو کی حمایت کرتے ہیں۔ گارڈریل میں "ٹرپ وائر" ہو سکتا ہے - اگر ٹرپ وائر کو متحرک کیا جاتا ہے، تو ایجنٹ کا عمل فوری طور پر بند ہو جائے گا اور گارڈریل ٹریپ وائر ٹریگرڈ استثناء اٹھایا جائے گا۔

یہ تاخیر کے لیے واقعی کارآمد ہے: مثال کے طور پر، آپ کے پاس ایک بہت تیز ماڈل ہو سکتا ہے جو گارڈریل چلاتا ہے اور ایک سست ماڈل جو اصل ایجنٹ کو چلاتا ہے۔ آپ سست ماڈل کے ختم ہونے کا انتظار نہیں کرنا چاہیں گے، لہذا گارڈریلز آپ کو غلط ان پٹس کو تیزی سے مسترد کرنے دیتے ہیں۔

مثالوں کے لیے input_guardrails.py اور output_guardrails.py فائلیں دیکھیں۔