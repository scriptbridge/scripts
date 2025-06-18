"""
# ScriptBridge.io 🚀
Turn plain English into powerful Python scripts for inventory, ERP, and finance automation.

### What It Does
ScriptBridge lets you describe a task like "get the last 10 sales orders from Fishbowl" and returns a working Python script using AI.

### Tech Stack
- Streamlit frontend
- OpenAI GPT-4 for script generation
- Python + dotenv

### Setup
```bash
git clone https://github.com/scriptbridge/core.git
cd core
pip install -r requirements.txt
cp config/.env.example .env
# Add your OpenAI API key
streamlit run app/streamlit_app.py
```
