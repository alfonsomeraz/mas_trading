# === market_thesis_agent/cli.py ===
import logging
import os
import argparse
from dotenv import load_dotenv
from agents.news_scraper import scrape_yahoo_finance_headlines
from agents.sentiment import analyze_sentiment
from agents.macro_signal import fetch_macro_data, analyze_macro_signals
from agents.thesis_generator import generate_market_thesis
from agents.ticker_watchlist import generate_watchlist

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MarketAgent")

def main(args):
    try:
        logger.info("📡 Scraping Yahoo Finance headlines...")
        headlines = scrape_yahoo_finance_headlines()
        print("Found raw headlines:", headlines[:20])


        if not headlines:
            logger.warning("No headlines found. Check scraping logic.")
            exit(1)

        logger.info("🔍 Running sentiment analysis...")
        sentiment_summary = analyze_sentiment(headlines)

        logger.info("🌐 Fetching macro data and analysis...")
        macro_data = fetch_macro_data()
        macro_summary = analyze_macro_signals(macro_data)

        logger.info("🧠 Generating market thesis using GPT...")
        thesis = generate_market_thesis(headlines)

        logger.info("📈 Generating ticker watchlist...")
        watchlist = generate_watchlist(thesis)

        if args.output == "console":
            print_results(sentiment_summary, macro_summary, thesis, watchlist)
        elif args.output == "file":
            save_results_to_file(sentiment_summary, macro_summary, thesis, watchlist, args.filepath)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        exit(1)

def print_results(sentiment_summary, macro_summary, thesis, watchlist):
    print("\n📊 Sentiment Analysis:\n" + "=" * 60)
    print(sentiment_summary)

    print("\n🌐 Macro View:\n" + "=" * 60)
    print(macro_summary)

    print("\n📝 Today's Market Thesis:\n" + "=" * 60)
    print(thesis)

    print("\n📈 Ticker Watchlist:\n" + "=" * 60)
    print(watchlist)
    print("=" * 60)

def save_results_to_file(sentiment_summary, macro_summary, thesis, watchlist, filepath):
    try:
        with open(filepath, "w") as file:
            file.write("📊 Sentiment Analysis:\n" + "=" * 60 + "\n")
            file.write(sentiment_summary + "\n\n")

            file.write("🌐 Macro View:\n" + "=" * 60 + "\n")
            file.write(macro_summary + "\n\n")

            file.write("📝 Today's Market Thesis:\n" + "=" * 60 + "\n")
            file.write(thesis + "\n\n")

            file.write("📈 Ticker Watchlist:\n" + "=" * 60 + "\n")
            file.write(watchlist + "\n")
        logger.info(f"Results saved to {filepath}")
    except IOError as e:
        logger.error(f"Failed to save results to file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Market Thesis Agent CLI")
    parser.add_argument(
        "--output", 
        choices=["console", "file"], 
        default="console", 
        help="Output results to console or file"
    )
    parser.add_argument(
        "--filepath", 
        type=str, 
        default="results.txt", 
        help="Filepath to save results if output is 'file'"
    )
    args = parser.parse_args()

    main(args)

