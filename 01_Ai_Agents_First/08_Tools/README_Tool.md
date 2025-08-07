Tutorial_12

https://youtu.be/lm1vTwvt2Po?list=PLHe-tEq_b1rL54y4DB4tK5E7zebr9G4Nw

Data Types :

1.Non Real Time Data (Historical Data)
["Poorani Baatein Example Pakistan Ka Founder Kon Hai?"]

2.Real Time Data (Current Update)
["currency Rate, Current Date, Weather Update"]

3.Persnalised Data (Personal Information)
["Resume, Company Data, Students Details"]

Terminal OutPut

result = Runner.run_sync(agent,
                         "Who Is The Founder Of Pakistan?'\n"
                         "What Is The Conversion Rate Of USD To PKR In Today's Date?\n"
                         "What Is The Weather In Pakistani Cities?\n"
                         "What Is The ToDay Date?\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me Top 10 Students In Class 10th\n"
                         "Show Me The Top 10 Novels By Mazher Kaleem M.A?/n"
                         "Information Urdu & English To All Sentences\n",
                        run_config=config)

print(result.final_output)


Okay, I can help you with these questions. However, please understand that some of these requests require real-time data that I may not have direct access to. Here's what I can do and what information I might need from you:

1.  **Who is the Founder of Pakistan?**

    *   The founder of Pakistan is **Muhammad Ali Jinnah**, also known as Quaid-e-Azam.      

2.  **What is the conversion rate of USD to PKR today?**

    *   I do not have access to real-time currency conversion rates. Currency rates fluctuate constantly. To get the most accurate and up-to-date information, please check reliable sources like:
        *   **Google Finance:** (Search "USD to PKR")
        *   **A reputable financial website:** (e.g., Bloomberg, Reuters, a major bank in Pakistan)
        *   **A currency converter tool:** (e.g., XE.com)

3.  **What is the weather in Pakistani cities?**

    *   I do not have access to real-time weather data. To get the current weather conditions and forecasts, please use these resources:
        *   **Google Weather:** (Search "Weather in [City Name], Pakistan")
        *   **A reliable weather app or website:** (e.g., AccuWeather, The Weather Channel)  
        *   **The Pakistan Meteorological Department website.**

4.  **What is today's date?**

    *   Today is Sunday, October 27, 2024.

5.  **Show me the top 10 students in class 10th.**

    *   I cannot provide this information. Information about student performance is confidential and not publicly available. To access this information, you would need to contact the school or educational institution directly.

6.  **Show me the top 10 novels by Mazher Kaleem M.A?**

    *   Here are 10 popular novels by Mazhar Kaleem M.A., particularly within the Imran Series:

        1.  **Baghlon Ka Ilaqa (بغلوں کا علاقہ)**
        2.  **Operation Desert Fire (آپریشن ڈیزرٹ فائر)**
        3.  **Khaufnak Imarat (خوفناک عمارت)**
        4.  **Lashon Ka Jungle (لاشوں کا جنگل)**
        5.  **Pechida Signal (پیچیدہ سگنل)**
        6.  **Sungla Island (سنگلا آئی لینڈ)**
        7.  **Dark Force (ڈارک فورس)**
        8.  **Point Number Zero (پوائنٹ نمبر زیرو)**
        9.  **Double White (ڈبل وائٹ)**
        10. **Golden Circle (گولڈن سرکل)**

        These novels are popular for their thrilling plots and are well-regarded within the Imran Series.

I hope this is helpful!

Terminal OutPut Weather_Agent.py

tools>>> FunctionTool(name='fetch_weather', description='fetch weather accroding to city\n\nArgs:\ncity: str', params_json_schema={'properties': {'city': {'title': 'City', 'type': 'string'}}, 'required': ['city'], 'title': 'fetch_weather_args', 'type': 'object', 'additionalProperties': False}, on_invoke_tool=<function function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x000001A1FC21CB80>, strict_json_schema=True, is_enabled=True)
Tracing is disabled. Not creating trace Agent workflow
Setting current trace: no-op
Parent None or <agents.tracing.traces.NoOpTrace object at 0x000001A1FC10EFD0> is no-op, returning NoOpSpan
Running agent Weather Assistant (turn 1)
Tracing is disabled. Not creating span <agents.tracing.span_data.GenerationSpanData object at 0x000001A1FC1F5EB0>
[
  {
    "content": "You are helpfull weather assisatnt provide answer by calling fetch weathe tool",
    "role": "system"
  },
  {
    "role": "user",
    "content": "what is the weather in karachi?"
  }
]
Tools:
[
  {
    "type": "function",
    "function": {
      "name": "fetch_weather",
      "description": "fetch weather accroding to city\n\nArgs:\ncity: str",
      "parameters": {
        "properties": {
          "city": {
            "title": "City",
            "type": "string"
          }
        },
        "required": [
          "city"
        ],
        "title": "fetch_weather_args",
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
        "arguments": "{\"city\":\"karachi\"}",
        "name": "fetch_weather"
      },
      "type": "function"
    }
  ]
}

Parent <agents.tracing.spans.NoOpSpan object at 0x000001A1FC200550> or <agents.tracing.traces.NoOpTrace object at 0x000001A1FC10EFD0> is no-op, returning NoOpSpan
Invoking tool fetch_weather with input {"city":"karachi"}
Tool call args: ['karachi'], kwargs: {}
Tool fetch_weather returned the weather in karachi is sunny
Running agent Weather Assistant (turn 2)
Tracing is disabled. Not creating span <agents.tracing.span_data.GenerationSpanData object at 0x000001A1FC628E30>
[
  {
    "content": "You are helpfull weather assisatnt provide answer by calling fetch weathe tool",
    "role": "system"
  },
  {
    "role": "user",
    "content": "what is the weather in karachi?"
  },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "",
        "type": "function",
        "function": {
          "name": "fetch_weather",
          "arguments": "{\"city\":\"karachi\"}"
        }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "",
    "content": "the weather in karachi is sunny"
  }
]
Tools:
[
  {
    "type": "function",
    "function": {
      "name": "fetch_weather",
      "description": "fetch weather accroding to city\n\nArgs:\ncity: str",
      "parameters": {
        "properties": {
          "city": {
            "title": "City",
            "type": "string"
          }
        },
        "required": [
          "city"
        ],
        "title": "fetch_weather_args",
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
  "content": "The weather in karachi is sunny.\n",
  "refusal": null,
  "role": "assistant",
  "annotations": null,
  "audio": null,
  "function_call": null,
  "tool_calls": null
}

Resetting current trace
result>>> The weather in karachi is sunny.

Shutting down trace provider
Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x000001A1FB501940>  