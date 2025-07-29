Handoff

https://openai.github.io/openai-agents-python/handoffs/

In the OpenAI Agents SDK, handoffs enable an agent to delegate tasks to another agent, facilitating specialized handling of different tasks within a multi-agent system. This mechanism is particularly useful when different agents possess expertise in distinct domains. citeturn0search2

Table of Contents:

1.    Understanding Handoffs
2.    Creating Agents
3.    Implementing Handoffs
4.    Running the Agent Orchestration
5.    Advanced Handoff Customization
6.    Conclusion

1. Understanding Handoffs

Handoffs allow an agent to delegate tasks to another agent. This is particularly useful in scenarios where different agents specialize in distinct areas. For example, a customer support application might have agents that each specifically handle tasks like order status, refunds, or frequently asked questions.

2. Creating Agents

Define agents with specific roles and instructions.

Examples

3. Implementing Handoffs

To enable an agent to delegate tasks to another agent, define handoffs during the agent's creation.

Examples

In this setup, the triage_agent can delegate tasks to either the billing_agent or the refund_agent based on the user's request.

4. Running the Agent Orchestration

Use the Runner to execute the agent workflow.

Examples

In this example, the triage_agent assesses the user's input and delegates the task to the appropriate specialist agent.

Note:

Triage AI agents are artificial intelligence systems designed to assess, categorize, and prioritize tasks, ensuring that the most critical issues receive immediate attention. By automating the initial evaluation process, these agents enhance efficiency and accuracy across various sectors. How to pronounce:

https://www.google.com/search?q=pronounce+triage

5. Advanced Handoff Customization

For more control over handoffs, utilize the handoff() function to customize behavior.

Examples


In this scenario, the triage_agent uses a customized handoff to the refund_agent, allowing for specific configurations during the delegation process.

6. Conclusion

Implementing handoffs in the OpenAI Agents SDK enhances the modularity and specialization of your AI agents, enabling them to delegate tasks efficiently. By following this tutorial, you can create a multi-agent system where each agent operates within its domain expertise, leading to more efficient and effective task management.

For more detailed information, refer to the OpenAI Agents SDK Handoffs Documentation.

https://openai.github.io/openai-agents-python/handoffs/


ہینڈ آف

https://openai.github.io/openai-agents-python/handoffs/

OpenAI ایجنٹس SDK میں، ہینڈ آف ایک ایجنٹ کو کام دوسرے ایجنٹ کو سونپنے کے قابل بناتا ہے، جس سے ملٹی ایجنٹ سسٹم کے اندر مختلف کاموں کی خصوصی ہینڈلنگ میں سہولت ہوتی ہے۔ یہ طریقہ کار خاص طور پر مفید ہے جب مختلف ایجنٹوں کو الگ الگ ڈومینز میں مہارت حاصل ہو۔ citeturn0search2

مندرجات کا جدول: 

 1 . ہینڈ آف کو سمجھنا 

 2 . ایجنٹ بنانا 

 3 . ہینڈ آف کو نافذ کرنا 

 4 . ایجنٹ آرکیسٹریشن چلانا 

 5 . اعلی درجے کی ہینڈ آف حسب ضرورت 

 6 . نتیجہ 


 1 . ہینڈ آف کو سمجھنا

ہینڈ آف ایک ایجنٹ کو کام دوسرے ایجنٹ کو سونپنے کی اجازت دیتا ہے۔ یہ خاص طور پر ایسے حالات میں مفید ہے جہاں مختلف ایجنٹ الگ الگ علاقوں میں مہارت رکھتے ہیں۔ مثال کے طور پر، کسٹمر سپورٹ ایپلی کیشن میں ایسے ایجنٹ ہو سکتے ہیں جو ہر ایک خاص طور پر آرڈر کی حیثیت، رقم کی واپسی، یا اکثر پوچھے جانے والے سوالات جیسے کاموں کو ہینڈل کرتے ہیں۔ 

ایجنٹ بنانا

مخصوص کرداروں اور ہدایات کے ساتھ ایجنٹوں کی وضاحت کریں۔

مثالیں 

ہینڈ آف کو نافذ کرنا

کسی ایجنٹ کو دوسرے ایجنٹ کو کام سونپنے کے قابل بنانے کے لیے، ایجنٹ کی تخلیق کے دوران ہینڈ آف کی وضاحت کریں۔

مثالیں

اس سیٹ اپ میں، triage_agent صارف کی درخواست کی بنیاد پر یا تو بلنگ_ایجنٹ یا ریفنڈ_ایجنٹ کو کام سونپ سکتا ہے۔ 4. ایجنٹ آرکیسٹریشن چلانا

ایجنٹ کے ورک فلو کو انجام دینے کے لیے رنر کا استعمال کریں۔

مثالیں

اس مثال میں، triage_agent صارف کے ان پٹ کا اندازہ لگاتا ہے اور مناسب ماہر ایجنٹ کو کام سونپتا ہے۔

نوٹ:

Triage AI ایجنٹس مصنوعی ذہانت کے نظام ہیں جو کاموں کی تشخیص، درجہ بندی اور ترجیح دینے کے لیے بنائے گئے ہیں، اس بات کو یقینی بناتے ہوئے کہ انتہائی نازک مسائل پر فوری توجہ دی جائے۔ ابتدائی تشخیص کے عمل کو خودکار بنا کر، یہ ایجنٹ مختلف شعبوں میں کارکردگی اور درستگی کو بڑھاتے ہیں۔ کس طرح تلفظ کریں:

https://www.google.com/search?q=pronounce+triage 

اعلی درجے کی ہینڈ آف حسب ضرورت

ہینڈ آف پر مزید کنٹرول کے لیے، ہینڈ آف() فنکشن کو استعمال کریں تاکہ رویے کو اپنی مرضی کے مطابق بنایا جا سکے۔

مثالیں

اس منظر نامے میں، ٹرائیج_ایجنٹ ریفنڈ_ایجنٹ کو اپنی مرضی کے مطابق ہینڈ آف کا استعمال کرتا ہے، جس سے وفد کے عمل کے دوران مخصوص کنفیگریشنز کی اجازت ملتی ہے۔ 6. نتیجہ

OpenAI ایجنٹس SDK میں ہینڈ آف کو لاگو کرنا آپ کے AI ایجنٹوں کی ماڈیولریٹی اور تخصص کو بڑھاتا ہے، جس سے وہ کاموں کو مؤثر طریقے سے سونپ سکتے ہیں۔ اس ٹیوٹوریل پر عمل کرکے، آپ ایک ملٹی ایجنٹ سسٹم بنا سکتے ہیں جہاں ہر ایجنٹ اپنی ڈومین کی مہارت کے اندر کام کرتا ہے، جس سے زیادہ موثر اور موثر ٹاسک مینجمنٹ ہوتا ہے۔

مزید تفصیلی معلومات کے لیے، OpenAI ایجنٹس SDK Handoffs Documentation سے رجوع کریں۔

https://openai.github.io/openai-agents-python/handoffs/
