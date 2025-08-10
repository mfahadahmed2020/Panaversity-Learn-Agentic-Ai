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


    ایجنٹ لوپ



ایجنٹ لوپ ایجنٹ لوپ
لائف سائیکل

عام اصطلاحات میں، لائف سائیکل سے مراد ان مراحل کی مکمل ترتیب ہے جس سے کوئی شے، عمل، یا ہستی اپنی تخلیق سے اس کے خاتمے تک گزرتی ہے۔

OpenAI ایجنٹس SDK کے تناظر میں، یہ خاص طور پر ان مراحل کو بیان کرتا ہے جن کا ایجنٹ تجربہ کرتا ہے — جب سے یہ شروع کیا جاتا ہے (یا چالو کیا جاتا ہے) جب تک کہ یہ اپنا کام مکمل نہ کر لے اور آؤٹ پٹ پیدا نہ کر دے۔
لائف سائیکل واقعات (ہکس)

کبھی کبھی، آپ ایک ایجنٹ کے لائف سائیکل کا مشاہدہ کرنا چاہتے ہیں۔ مثال کے طور پر، آپ واقعات کو لاگ کرنا چاہتے ہیں، یا کچھ واقعات پیش آنے پر ڈیٹا کو پہلے سے بازیافت کرنا چاہتے ہیں۔ آپ ہکس پراپرٹی کے ساتھ ایجنٹ کے لائف سائیکل کو جوڑ سکتے ہیں۔ AgentHooks کلاس کو سب کلاس کریں، اور ان طریقوں کو اوور رائیڈ کریں جن میں آپ کی دلچسپی ہے۔

OpenAI ایجنٹس SDK میں، لائف سائیکل مینجمنٹ دو سطحوں پر فراہم کی جاتی ہے: 

رن لیول لائف سائیکل (رن ہکس): 
یہ ان عالمی واقعات کا انتظام کرتا ہے جو ایک یا زیادہ ایجنٹوں کے پورے عمل یا "رن" پر محیط ہوتے ہیں۔ یہ آپ کو اہم واقعات کی نگرانی اور کنٹرول کرنے کی اجازت دیتا ہے جیسے ایجنٹ کے عمل کے آغاز اور اختتام، ٹول کی درخواستیں، اور ایجنٹوں کے درمیان ہینڈ آف۔ 

ایجنٹ لیول لائف سائیکل (AgentHooks): 
یہ انفرادی ایجنٹ پر مرکوز ہے۔ یہ آپ کو ایجنٹ کے مخصوص ورک فلو میں اپنی مرضی کے مطابق منطق داخل کرنے دیتا ہے — ٹریکنگ ایونٹس جیسے کہ ایجنٹ کب پروسیسنگ شروع کرتا ہے، کب وہ اپنا کام مکمل کرتا ہے، اور جب وہ بیرونی ٹولز کے ساتھ تعامل کرتا ہے۔

یہ دونوں پرتیں نظام کے عمل کے وسیع نظریہ (رن ہُکس کے ذریعے) اور ہر ایجنٹ کے رویے پر (AgentHooks کے ذریعے) ایک تفصیلی، عمدہ کنٹرول دونوں کی اجازت دیتی ہیں۔
OpenAI ایجنٹس SDK میں لائف سائیکل چلائیں۔

SDK میں، رن لائف سائیکل کا انتظام RunHooks کے ذریعے کیا جاتا ہے۔ یہ ہکس آپ کو ایسے واقعات کا مشاہدہ اور کنٹرول کرنے کی اجازت دیتے ہیں جو ایک یا زیادہ ایجنٹوں کے پورے دور میں رونما ہوتے ہیں۔ ان میں کال بیکس شامل ہیں جب کوئی ایجنٹ شروع ہوتا ہے یا ختم ہوتا ہے، جب کوئی ٹول چلنے والا ہوتا ہے، اور جب ایجنٹوں کے درمیان کنٹرول ختم ہوتا ہے۔ آپ ان (لائف سائیکل ایونٹس) پر کال بیکس شامل کر سکتے ہیں[https://openai.github.io/openai-agents-python/ref/lifecycle/#agents.lifecycle.RunHooks] 

on_agent_start async: ایجنٹ کو طلب کرنے سے پہلے کال کی جاتی ہے۔ موجودہ ایجنٹ کے تبدیل ہونے پر ہر بار کال کی جاتی ہے۔ 
on_agent_end async: اس وقت کال کیا جاتا ہے جب ایجنٹ حتمی آؤٹ پٹ تیار کرتا ہے۔ 
on_handoff async: ہینڈ آف ہونے پر کال کیا جاتا ہے۔ 
on_tool_start async: کسی ٹول کو شروع کرنے سے پہلے کال کی جاتی ہے۔ 
on_tool_end async: کسی ٹول کو استعمال کرنے کے بعد کال کی جاتی ہے۔


