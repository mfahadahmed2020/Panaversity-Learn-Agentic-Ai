import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import json


load_dot_env()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is Missing in .env")

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("Chat History", [])
    await cl.Message(content="Welcome To The ** Translator Agent By M Fahad Ahmed ** !\n\n Please Tell Me ** WHAT You Want You Want To Translate ** & ** In To Which Language ? ** ").send()

@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content=" Translating....!")
    await msg.send()
    
    history = cl.user_session.get("Chat History") or []

    try:
        response = await completion(
            model="gemini/gemini-1.5-Flash",
            api_key=gemini_api_key,
            messages=history
        )
        response_content = response.choices[0].message.content
        msg.content = response_content
        await msg.update()
        history.append({"Role": "Assistant", "Content": response_content})
        cl.user_session.set("Chat_History", history)

    except Exception as e:
        msg.content = f" Error: {str(e)}"
        await msg.update()
        
        @cl.on_chat_end
        async def on_chat_end():
            history = cl.user_session.get("Chat_History") or []
            with open("Translation_Chat_History.json", "w") as f:
                json.dump(history, f, indent=2)

            print("Chat history saved")