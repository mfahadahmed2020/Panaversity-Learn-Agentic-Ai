01.Structured_OutPut.py

Terminal Out Put

Creating trace Agent workflow with id trace_4fed5eab0ace4429845a6735399c138d

Setting current trace: trace_4fed5eab0ace4429845a6735399c138d

Creating span <agents.tracing.span_data.AgentSpanData object at 0x000001C9D78C4640> with id None      

Running agent Structured_Weather_Agent (turn 1)

Creating span <agents.tracing.span_data.GenerationSpanData object at 0x000001C9D79488F0> with id None 

[
  {
    "content": "Use the final_output tool with WeatherAnswer schema.",
    "role": "system"
  },
  {
    "role": "user",
    "content": "Tell me karachi's temperature?."   
  }
]

Tools:

[]

Stream: False

Tool choice: NOT_GIVEN

Response format: {'type': 'json_schema', 'json_schema': {'name': 'final_output', 'strict': True, 'schema': {'properties': {'location': {'title': 'Location', 'type': 'string'}, 'temperature_c': {'title': 'Temperature C', 'type': 'number'}, 'summary': {'title': 'Summary', 'type': 'string'}}, 'required': ['location', 'temperature_c', 'summary'], 'title': 'WeatherAnswer', 'type': 'object', 'additionalProperties': False}}}

Skipping Trace Export

LLM resp:

{
  "content": "{\n  \"location\": \"Karachi\",\n  \"summary\": \"Sunny\",\n  \"temperature_c\": 32.0\n}",
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": null
}

Resetting current trace

Creating trace Agent workflow with id trace_9b4826b9303d49cdb169120a803d7133

Setting current trace: trace_9b4826b9303d49cdb169120a803d7133

Creating span <agents.tracing.span_data.AgentSpanData object at 0x000001C9D77D5540> with id None      

Running agent Simple_Agent (turn 1)

Creating span <agents.tracing.span_data.GenerationSpanData object at 0x000001C9D7917CB0> with id None 

[
  {
    "content": "You are a helpfull asssistant.",   
    "role": "system"
  },
  {
    "role": "user",
    "content": "Hello?"
  }
]

Tools:

[]

Stream: False

Tool choice: NOT_GIVEN

Response format: NOT_GIVEN

LLM resp:

{
  "content": "Hello! How can I help you today?\n", 
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": null
}

Resetting current trace

location='Karachi' temperature_c=32.0 summary='Sunny'
32.0

<class '__main__.WeatherAnswer'>
======================================================================

Hello! How can I help you today?

<class 'str'>

Shutting down trace provider

Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x000001C9D6B5ACF0>   

Urdu Traslation in Terminal


ID ٹریس کے ساتھ ٹریس ایجنٹ ورک فلو بنانا
موجودہ ٹریس سیٹ کرنا
ٹریس
اسپین بنانا
ایجنٹ اسپین ڈیٹا کو ٹریس کر رہے ہیں ایجنٹ اسپین ڈیٹا آبجیکٹ پر آئی ڈی کے ساتھ کوئی نہیں۔
رننگ ایجنٹ سٹرکچرڈ ویدر ایجنٹ ٹرن بنا رہا ہے اسپین <ایجنٹس ٹریسنگ اسپین ڈیٹا جنریشن اسپین ڈیٹا آبجیکٹ پر id کے ساتھ کوئی بھی مواد نہیں WeatherAnswer اسکیما کے ساتھ حتمی آؤٹ پٹ ٹول استعمال کریں
کردار کا نظام
کردار صارف کا مواد مجھے کراچی کا درجہ حرارت بتائیں؟
اوزار:
سلسلہ غلط
ٹول کا انتخاب نہیں دیا گیا۔
رسپانس فارمیٹ {'type': 'json_schema', 'json_schema': {'name': 'final_output', 'strict': True, 'schema': {'properties': {'location': {'title': 'Location', 'type': 'string'}, 'temperature'c':': 'Temperature'c':' 'number'}, 'summary': {'title': 'Summary', 'type': 'string'}}, 'required': ['location', 'temperature_c', 'summary'], 'title': 'WeatherAnswer', 'type': 'object', 'additionalProperties':}}

OPENAI_API_KEY سیٹ نہیں ہے، ٹریس ایکسپورٹ کو چھوڑ رہا ہے۔
ایل ایل ایم جواب:
{ 
"content": "{\n \"مقام\": \"کراچی\"،\n \"خلاصہ\": \"دھوپ\"،\n \"درجہ حرارت_c\": 32.0\n}", 
"انکار": null، 
"role": "معاون" 
"تشریحات": null، 
"آڈیو": null، 
"function_call": null، 
"tool_calls": null
}

موجودہ ٹریس کو دوبارہ ترتیب دیا جا رہا ہے۔
id trace_9b4826b9303d49cdb169120a803d7133 کے ساتھ ٹریس ایجنٹ ورک فلو بنانا
موجودہ ٹریس ترتیب دینا: trace_9b4826b9303d49cdb169120a803d7133
id None کے ساتھ span <agents.tracing.span_data.AgentSpanData آبجیکٹ 0x000001C9D77D5540> بنانا
رننگ ایجنٹ Simple_Agent (ٹرن 1)
id None کے ساتھ span <agents.tracing.span_data.GenerationSpanData آبجیکٹ 0x000001C9D7917CB0> بنانا
[ 
{ 
"content": "آپ ایک مددگار معاون ہیں۔", 
"کردار": "نظام" 
}، 
{ 
"role": "صارف" 
"content": "ہیلو؟" 
}
]
اوزار:
[ ]
سلسلہ: غلط
ٹول کا انتخاب: NOT_GIVEN
جواب کی شکل: NOT_GIVEN

ایل ایل ایم جواب:
{ 
"content": "ہیلو! آج میں آپ کی مدد کیسے کر سکتا ہوں؟\n", 
"انکار": null، 
"role": "معاون" 
"تشریحات": null، 
"آڈیو": null، 
"function_call": null، 
"tool_calls": null
}

موجودہ ٹریس کو دوبارہ ترتیب دیا جا رہا ہے۔
مقام='کراچی' درجہ حرارت_c=32.0 خلاصہ='دھوپ'
32.0

<class '__main__.WeatherAnswer'>
==========================================================
ہیلو! آج میں آپ کی مدد کیسے کر سکتا ہوں؟

<کلاس 'str'>
ٹریس فراہم کنندہ کو بند کیا جا رہا ہے۔
ٹریس پروسیسر کو بند کیا جا رہا ہے <agents.tracing.processors.BatchTraceProcessor آبجیکٹ پر


02.Prompt.py

Terminal Out Put :

Creating trace Agent workflow with id trace_05b09eaa2a5c427abe8c01e14ad78e30

Setting current trace: trace_05b09eaa2a5c427abe8c01e14ad78e30

Creating span <agents.tracing.span_data.AgentSpanData object at 0x0000025290C3D680> with id None

Running agent Math Agent (turn 1)

Creating span <agents.tracing.span_data.GenerationSpanData object at 0x0000025290CC8950> with id None        

[
  {
    "role": "user",
    "content": "Tell me the best tourist spots of paris in list and short."
  }
]
Tools:
[]

Stream: False

Tool choice: NOT_GIVEN

Response format: NOT_GIVEN

LLM resp:

{
  "content": "Okay, here's a list of the best tourist spots in Paris, with short descriptions:\n\n*   **Eiffel Tower:** Iconic landmark, stunning city views.\n\n*   **Louvre Museum:** Home to masterpieces like the Mona Lisa.\n\n*   **Arc de Triomphe:** Triumphal arch at the end of the Champs-Élysées.\n\n*   **Champs-Élysées:** Famous avenue, shopping, dining.\n\n*   **Notre Dame Cathedral:** Historic cathedral, beautiful architecture (currently under renovation).\n\n*   **Sainte-Chapelle:** Stunning Gothic chapel with stained glass.\n\n*  

 **Montmartre & Sacré-Cœur Basilica:** Artistic neighborhood, hilltop basilica.\n\n*   **Musée d'Orsay:** Impressionist art in a former train station.\n\n*   **Seine River Cruise:** Relaxing way to see the city's landmarks.\n\n*   **Latin Quarter:** Historic student district, vibrant atmosphere.\n\n*   **Luxembourg Gardens:** Beautiful gardens, perfect for relaxing.\n\n*   **Palace of Versailles:** Opulent palace, former royal residence (a bit outside Paris).\n",
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": null
}

Resetting current trace

🤖 CALLING AGENT

Okay, here's a list of the best tourist spots in Paris, with short descriptions:

*   **Eiffel Tower:** Iconic landmark, stunning city views.

*   **Louvre Museum:** Home to masterpieces like the Mona Lisa.

*   **Arc de Triomphe:** Triumphal arch at the end of the Champs-Élysées.

*   **Champs-Élysées:** Famous avenue, shopping, dining.

*   **Notre Dame Cathedral:** Historic cathedral, beautiful architecture (currently under renovation).       

*   **Sainte-Chapelle:** Stunning Gothic chapel with stained glass.

*   **Montmartre & Sacré-Cœur Basilica:** Artistic neighborhood, hilltop basilica.

*   **Musée d'Orsay:** Impressionist art in a former train station.

*   **Seine River Cruise:** Relaxing way to see the city's landmarks.

*   **Latin Quarter:** Historic student district, vibrant atmosphere.

*   **Luxembourg Gardens:** Beautiful gardens, perfect for relaxing.

*   **Palace of Versailles:** Opulent palace, former royal residence (a bit outside Paris).


03.Stop_At_Tools.py

Terminal Out Put 

======================================================================

Today's weather of karachi is sunny.


04.Structured_Tools.py

Terminal Out Put

Creating trace Agent workflow with id trace_e5a85f4fa36241078de16385c7d65568

Setting current trace: trace_e5a85f4fa36241078de16385c7d65568

Creating span <agents.tracing.span_data.AgentSpanData object at 0x0000024D11265E00> with id None

Running agent Assistant (turn 1)
Creating span <agents.tracing.span_data.GenerationSpanData object at 0x0000024D12D10D10> with id None        

[
  {
    "content": "You are a helpful assistant. Always use tools for math questions and follow DMAS rule and explainclearly.",
    "role": "system"
  },
  {
    "role": "user",
    "content": "What is 5 - 10 + 15?"
  }
]

Tools:

[
  {
    "type": "function",
    "function": {
      "name": "add",
      "description": "Add two numbers exactly.",
      "parameters": {
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "add_args",
        "type": "object",
        "additionalProperties": false
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "subtract",
      "description": "Subtract two numbers exactly.",
      "parameters": {
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "subtract_args",
        "type": "object",
        "additionalProperties": false
      }
    }
  }
]

Stream: False

Tool choice: NOT_GIVEN

Response format: NOT_GIVEN

LLM resp:

{
  "content": null,
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": [
    {
      "id": "",
      "function": {
        "arguments": "{\"a\":5,\"b\":10}",
        "name": "subtract"
      },
      "type": "function"
    }
  ]
}

Creating span <agents.tracing.span_data.FunctionSpanData object at 0x0000024D110FEC10> with id None

Invoking tool subtract with input {"a":5,"b":10}

Tool call args: [5, 10], kwargs: {}


Tool subtract returned -5

Running agent Assistant (turn 2)

Creating span <agents.tracing.span_data.GenerationSpanData object at 0x0000024D13194FB0> with id None        

[
  {
    "content": "You are a helpful assistant. Always use tools for math questions and follow DMAS rule and explainclearly.",
    "role": "system"
  },
  {
    "role": "user",
    "content": "What is 5 - 10 + 15?"
  },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "",
        "type": "function",
        "function": {
          "name": "subtract",
          "arguments": "{\"a\":5,\"b\":10}"
        }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "",
    "content": "-5"
  }
]
Tools:
[
  {
    "type": "function",
    "function": {
      "name": "add",
      "description": "Add two numbers exactly.",
      "parameters": {
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "add_args",
        "type": "object",
        "additionalProperties": false
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "subtract",
      "description": "Subtract two numbers exactly.",
      "parameters": {
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "subtract_args",
        "type": "object",
        "additionalProperties": false
      }
    }
  }
]
Stream: False
Tool choice: NOT_GIVEN
Response format: NOT_GIVEN

LLM resp:
{
  "content": null,
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": [
    {
      "id": "",
      "function": {
        "arguments": "{\"b\":15,\"a\":-5}",
        "name": "add"
      },
      "type": "function"
    }
  ]
}

Creating span <agents.tracing.span_data.FunctionSpanData object at 0x0000024D110FD360> with id None

Invoking tool add with input {"b":15,"a":-5}

Tool call args: [-5, 15], kwargs: {}

Tool add returned 10

Running agent Assistant (turn 3)

Creating span <agents.tracing.span_data.GenerationSpanData object at 0x0000024D131968D0> with id None        
[
  {
    "content": "You are a helpful assistant. Always use tools for math questions and follow DMAS rule and explainclearly.",
    "role": "system"
  },
  {
    "role": "user",
    "content": "What is 5 - 10 + 15?"
  },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "",
        "type": "function",
        "function": {
          "name": "subtract",
          "arguments": "{\"a\":5,\"b\":10}"
        }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "",
    "content": "-5"
  },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "",
        "type": "function",
        "function": {
          "name": "add",
          "arguments": "{\"b\":15,\"a\":-5}"
        }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "",
    "content": "10"
  }
]
Tools:
[
  {
    "type": "function",
    "function": {
      "name": "add",
      "description": "Add two numbers exactly.",
      "parameters": {
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "add_args",
        "type": "object",
        "additionalProperties": false
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "subtract",
      "description": "Subtract two numbers exactly.",
      "parameters": {
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "subtract_args",
        "type": "object",
        "additionalProperties": false
      }
    }
  }
]
Stream: False
Tool choice: NOT_GIVEN
Response format: NOT_GIVEN

Skipping Trace Export

LLM resp:

{
  "content": "First, subtract 10 from 5, which results in -5. Then, add 15 to -5, which results in 10. So, 5 
- 10 + 15 = 10.\n",
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": null
}

Resetting current trace

🤖 CALLING AGENT

First, subtract 10 from 5, which results in -5. Then, add 15 to -5, which results in 10. So, 5 - 10 + 15 = 10.

Shutting down trace provider

Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at skipping trace export.

![alt text](tool_calling-1.png)

Ye Ek Structured Object Hota Hai Jo Sirf System Prompt Nahi, Balke Pura Conversation Ka Format Define Karta Hai :

01.System Message.

02.User Message(s).

03.Tools Description.

04.Context Messages.
05.Response Formatting.

06.LLM Ko Ek Proper "Multi-Message" InPut Milta Hai, Jo Advanced APIs Jaise OpenAI Responses API ___Kay Liye Optimized Hota Hai.
