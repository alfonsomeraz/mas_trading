# agents/macro_signal.py
from openai import OpenAI
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fetch_macro_data():
    # Sample indicators (can expand this later)
    macro_context = {}

    try:
        oil = requests.get("https://api.api-ninjas.com/v1/commodityprice?symbol=oil", 
            headers={"X-Api-Key": os.getenv("NINJA_API_KEY")}).json()
        macro_context["Oil Price"] = f"${oil['price']}" if oil else "N/A"
    except:
        macro_context["Oil Price"] = "Error fetching"

    # You could add: 10Y treasury yield, inflation, jobs, etc.
    macro_context["10Y Yield"] = "4.25%"  # Placeholder for now

    return macro_context

def analyze_macro_signals(macro_data):
    formatted = "\\n".join(f"{k}: {v}" for k, v in macro_data.items())
    prompt = f"""
Here are some current macroeconomic signals for {datetime.now().strftime('%B %d')}:

{formatted}

Based on these, provide a market-level analysis: what sectors may benefit or suffer, and how risk sentiment might shift today.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a macro strategist analyzing current market conditions."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
