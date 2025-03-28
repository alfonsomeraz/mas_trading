# agents/sentiment.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(headlines):
    prompt = f"""
You are a financial sentiment analysis expert. Evaluate the sentiment of each headline below on a scale from -1 (very bearish) to +1 (very bullish). Then provide an average score.

Return the result in this format:
[
  {{ "headline": "...", "sentiment": 0.5 }},
  ...
]
Average sentiment: <score>
{chr(10).join(f'- {h}' for h in headlines)}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You analyze financial sentiment."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
