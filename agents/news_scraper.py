# agents/news_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_yahoo_finance_headlines():
    url = "https://finance.yahoo.com/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for link in soup.find_all("a"):
        text = link.get_text(strip=True)
        if text and len(text) > 30:
            headlines.append(text)

    # Filter duplicates & irrelevant junk
    cleaned = list(dict.fromkeys([h for h in headlines if "Yahoo" not in h and "Privacy" not in h]))
    return cleaned[:10]
