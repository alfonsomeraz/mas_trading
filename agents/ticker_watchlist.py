# agents/ticker_watchlist.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_watchlist(thesis_text):
    prompt = f"""
Based on the following market thesis, generate a focused watchlist of 3–5 stock tickers. 
Include the ticker, direction (long/short/neutral), and a one-line justification.

Market Thesis:
\"\"\"
{thesis_text}
\"\"\"
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a trading assistant who recommends tickers based on market themes."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
