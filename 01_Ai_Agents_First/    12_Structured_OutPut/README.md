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

OPENAI_API_KEY is not set, skipping trace export
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