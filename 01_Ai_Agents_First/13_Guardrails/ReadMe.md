PIAIC Agent with Guardrails (Jupyter Notebook)

This project implements a PIAIC (Presidential Initiative for Artificial Intelligence and Computing) agent using the OpenAI Agents SDK within a Jupyter Notebook (piaic-guardrails-example.ipynb). The agent is restricted to handling PIAIC-related queries (e.g., AI, Cloud Computing, Blockchain, IoT) through custom input and output guardrails.
Overview

    Purpose: Ensure the agent processes and responds only to PIAIC-related topics.
    Guardrails:
        Input Guardrail: Verifies that user input is relevant to PIAIC topics.
        Output Guardrail: Confirms the agent's response is PIAIC-relevant.
    Implementation: Uses dedicated guardrail agents to assess input/output relevance, with tripwires to stop off-topic content.
    Format: Jupyter Notebook for interactive development and testing.

Key Components

    PIAIC Agent: Core agent for answering PIAIC-related questions.
    Input Guardrail Agent: Checks input relevance to PIAIC.
    Output Guardrail Agent: Ensures response relevance to PIAIC.
    Notebook Structure: Combines markdown explanations with executable code cells.

Usage

Access the Notebook:

    Run the notebook directly in Google Colab: PIAIC Guardrails Example.
    Alternatively, download piaic-guardrails-example.ipynb and open it in Jupyter Notebook or JupyterLab.

Prerequisites:

    For local execution, install Jupyter Notebook/JupyterLab and required packages:

    pip install notebook agents pydantic

    Run the Notebook:
        In Colab or Jupyter, execute cells sequentially to:
            Import libraries
            Define the guardrail output model
            Create guardrail agents and functions
            Configure the main PIAIC agent
            Test with sample inputs

  Example Inputs:
        PIAIC-relevant: "What is the curriculum for PIAIC's AI course?"
        Non-PIAIC: "How do I bake a chocolate cake?"

  Output

    PIAIC-relevant inputs produce responses if both guardrails pass.
    Non-PIAIC inputs or outputs trigger a tripwire, showing an error (e.g., "Input Guardrail tripped: Input is not PIAIC-related.").

  File Structure

    piaic-guardrails-example.ipynb: Jupyter Notebook with the agent and guardrail implementation.

  Notes

    Utilizes OpenAI Agents SDK's InputGuardrail and OutputGuardrail classes.
    The PIAICRelevanceOutput model structures guardrail outputs (boolean and reasoning).
    Notebook cells include markdown for clarity and are designed for sequential execution.
    Google Colab automatically manages the asyncio event loop for seamless execution.

    PIAIC ایجنٹ گارڈریلز کے ساتھ (Jupyter Notebook)

یہ پروجیکٹ Jupyter نوٹ بک (piaic-guardrails-example.ipynb) کے اندر OpenAI ایجنٹس SDK کا استعمال کرتے ہوئے PIAIC (صدارتی اقدام برائے مصنوعی ذہانت اور کمپیوٹنگ) ایجنٹ کو نافذ کرتا ہے۔ ایجنٹ PIAIC سے متعلقہ سوالات (مثلاً، AI، Cloud Computing، Blockchain، IoT) کو کسٹم ان پٹ اور آؤٹ پٹ گارڈریلز کے ذریعے ہینڈل کرنے تک محدود ہے۔
جائزہ 

مقصد: ایجنٹ کے عمل کو یقینی بنائیں اور صرف PIAIC سے متعلقہ موضوعات پر جواب دیں۔ 
گارڈریلز: 
ان پٹ گارڈریل: اس بات کی تصدیق کرتا ہے کہ صارف کا ان پٹ PIAIC کے موضوعات سے متعلق ہے۔ 
آؤٹ پٹ گارڈریل: ایجنٹ کا جواب PIAIC سے متعلقہ ہونے کی تصدیق کرتا ہے۔ 
نفاذ: ان پٹ/آؤٹ پٹ کی مطابقت کا اندازہ لگانے کے لیے سرشار گارڈریل ایجنٹوں کا استعمال کرتا ہے، موضوع سے ہٹ کر مواد کو روکنے کے لیے ٹرپ وائرز کے ساتھ۔ 
فارمیٹ: انٹرایکٹو ترقی اور جانچ کے لیے Jupyter Notebook۔

کلیدی اجزاء 

PIAIC ایجنٹ: PIAIC سے متعلقہ سوالات کا جواب دینے کے لیے بنیادی ایجنٹ۔ 
ان پٹ گارڈریل ایجنٹ: پی آئی اے آئی سی سے ان پٹ کی مطابقت چیک کرتا ہے۔ 
آؤٹ پٹ گارڈریل ایجنٹ: PIAIC سے جواب کی مطابقت کو یقینی بناتا ہے۔ 
نوٹ بک کا ڈھانچہ: قابل عمل کوڈ سیلز کے ساتھ مارک ڈاون وضاحتوں کو جوڑتا ہے۔

استعمال

نوٹ بک تک رسائی: 

نوٹ بک کو براہ راست Google Colab میں چلائیں: PIAIC Guardrails کی مثال۔ 
متبادل طور پر، piaic-guardrails-example.ipynb ڈاؤن لوڈ کریں اور اسے Jupyter Notebook یا JupyterLab میں کھولیں۔

شرائط: 

مقامی عمل درآمد کے لیے، Jupyter Notebook/JupyterLab اور مطلوبہ پیکجز انسٹال کریں: 

پپ انسٹال نوٹ بک ایجنٹس پیڈینٹک 

نوٹ بک چلائیں: 
Colab یا Jupyter میں، سیلز کو ترتیب وار عمل میں لاتے ہیں: 
لائبریریاں درآمد کریں۔ 
گارڈریل آؤٹ پٹ ماڈل کی وضاحت کریں۔ 
گارڈریل ایجنٹس اور افعال بنائیں 
مرکزی PIAIC ایجنٹ کو ترتیب دیں۔ 
نمونے کے آدانوں کے ساتھ ٹیسٹ کریں۔ 

مثال کے ان پٹ: 
PIAIC سے متعلقہ: "PIAIC کے AI کورس کا نصاب کیا ہے؟" 
غیر PIAIC: "میں چاکلیٹ کیک کیسے بناؤں؟" 

آؤٹ پٹ 

PIAIC سے متعلقہ ان پٹ جوابات پیش کرتے ہیں اگر دونوں گارڈریل گزر جاتے ہیں۔ 
غیر PIAIC ان پٹس یا آؤٹ پٹس ٹرپ وائر کو متحرک کرتے ہیں، جو ایک خرابی دکھاتے ہیں (جیسے، "ان پٹ گارڈریل ٹرپ ہو گیا: ان پٹ PIAIC سے متعلق نہیں ہے۔")۔ 

فائل کا ڈھانچہ 

piaic-guardrails-example.ipynb: ایجنٹ اور گارڈریل کے نفاذ کے ساتھ Jupyter نوٹ بک۔ 

نوٹس 

OpenAI ایجنٹس SDK کی InputGuardrail اور OutputGuardrail کلاسز کا استعمال کرتا ہے۔ 
PIAICRelevanceOutput ماڈل گارڈریل آؤٹ پٹس (بولین اور استدلال) کا ڈھانچہ بناتا ہے۔ 
نوٹ بک سیلز میں وضاحت کے لیے مارک ڈاؤن شامل ہے اور ترتیب وار عمل درآمد کے لیے ڈیزائن کیے گئے ہیں۔ 
Google Colab بغیر کسی رکاوٹ کے عمل کے لیے asyncio ایونٹ لوپ کا خودکار طور پر انتظام کرتا ہے۔
