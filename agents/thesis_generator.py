# agents/thesis_generator.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_market_thesis(headlines):
    prompt = f"""
You are a financial analyst AI. Here are today's top market headlines:

{chr(10).join(f'- {h}' for h in headlines)}

Based on this information, generate a morning market thesis. 
Summarize key market themes, sectors affected, and suggest tickers to watch.
Format output as a clean summary.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a market analyst generating daily trade ideas."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
