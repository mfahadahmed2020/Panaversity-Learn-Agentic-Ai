M FAHAD AHMED

01_Ai_Agents_First

01_UV_Project_01 & 02

UV INSTALLATION GUIDE

Tutorial No = 01

https://www.youtube.com/watch?v=ARua6mP5Oks&list=PLHe-tEq_b1rL54y4DB4tK5E7zebr9G4Nw&index=4&pp=iAQB

Generative Ai Vs Agentic Ai

Generative Ai       Agentic Ai
Creating Content    Acting Autonomially
Based on Prompts    To Achieve Goals


Tutorial No = 02

https://www.youtube.com/watch?v=E0UEuUy_Iqg&list=PLHe-tEq_b1rL54y4DB4tK5E7zebr9G4Nw&index=8&pp=iAQB0gcJCdQJAYcqIYzv

How To Install UV In Python Setup Virtual Environment With Fastest Package Manager

UV Installation

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Windows Version
in powershell Run as Administrator
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
set the path no work in terminal search window
Enviorment Varriable
Edit the system enviornment Varriable
First Step of Enviorment Varriable
Second Step of Path Set & Select
Third Step of Edit
Forth Step of New (Your PC & LapTop & Mac User Directory Name Path Copy
Just Example : :Users\<yours pc my Name>\local\bin; Path cmd)
cmd command Prompt open check
uv --Version
Confirm
Check powershell open
First Step uv installed
Second Step UV Make The Folder Your Name
open folder simple cmd
code .
vs code open
open terminal
Forth Step UV Initialization

Usage: uv.exe [OPTIONS] <COMMAND>
Commands:
( run      Run a command or script
  init     Create a new project
  add      Add dependencies to the project
  remove   Remove dependencies from the project
  version  Read or update the project's version
  sync     Update the project's environment
  lock     Update the project's lockfile
  export   Export the project's lockfile to an alternate format
  tree     Display the project's dependency tree
  tool     Run and install commands provided by Python packages
  python   Manage Python versions and installations
  pip      Manage Python packages with a pip-compatible interface
  venv     Create a virtual environment
  build    Build Python packages into source distributions and wheels
  publish  Upload distributions to an index
  cache    Manage uv's cache
  self     Manage the uv executable
  help     Display documentation for a command)

New Projet Firs Time
UV init .
Same Folder Initialization project

Initialized Project `UV` at `C:\Users\PMLS\Desktop\UV`

virtual Enviorment
uv venv Create
Close To Open Every Time Activate
Active With: .venv\scripts\activate

UV Run main.py

Tutorial No = 03

https://youtu.be/9jjEy4YCND8?list=PLHe-tEq_b1rL54y4DB4tK5E7zebr9G4Nw

How To Get FREE Gemini API Key & Use It Google AI Gemini API For Beginners

Create .env
File Create
Enviorment Varriable

GEMINI_API_KEY = ''

Command Python packages
UV add python-dotenv

Free API KEY

Search: Google AI Studio
GEMINI API KEY 
Create Api KEY
Copy & Paste Vs Code in .env File

Tutorial No = 04

https://youtu.be/n3ba2LheuQc?list=PLHe-tEq_b1rL54y4DB4tK5E7zebr9G4Nw

Create Your First AI Agent 🤖 Step By Step Guide For Beginners 2025

Create First AI Agent
Steps
1.Install UV
2.Create Folder
3.Create Virtual Enviorment
4.Install Python Env packages
5.Create API KEY
6.Apply API KEY in .env
7.Install Open AI Agents
UV add openai-agents
8.Create Your First Agent
agent = Agent()
9.Connection With Your LLM
Large Language Model
Run Google GEMINI With OpenAi Agent SDK
syncronus
10.Execute/Run The Agent

Output

E:\Python Codes\Learn Agentic - AI\01_AI_Agents_First\04_Hello_Agent\SYNC - Hello_Agent>uv run m.py
RunResult:
- Last agent: Agent(name="Chief - X2 Translator", ...)
- Final output (str):
    My name is M. Fahad Ahmed. I am a student of GIAIC.

    **Urdu:**

    میرا نام ایم فہد احمد ہے۔ میں جی آئی اے آئی سی کا طالب علم ہوں۔
- 1 new item(s)
- 1 raw response(s)
- 0 input guardrail result(s)
- 0 output guardrail result(s)
(See `RunResult` for more details)