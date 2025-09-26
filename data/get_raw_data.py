import yfinance as yf
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

ticker = os.getenv("TICKER")
start_date = os.getenv("START_DATE")


# Should return df, save it for reasons, but no point to return ticker
def get_data(file_path: str, ticker: str=ticker, start: str=start_date, end: str=None)-> str:
    """
    returns ticker and file path of csv file (will return df) downloaded from Yahoo Finance, with data about stock market for certain ticker

    Args:
    file_path (str) -> path in which you want csv file to be saved
    ticker (str) -> company you want stock data from
    start (str) -> start date for data tbd (should be pd.DateTime)
    end (str) -> end date for data tbd (should be pd.DateTime)

    Returns:
    ticker name (should return df)
    """
    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')
    print(f"Getting data for {ticker} from {start} to {end}...")
    data = yf.download(ticker, start=start, end=end) # Download
    data.to_csv(file_path) # Save
    print(f"CSV file saved to: {file_path}")
    df = pd.read_csv(file_path, skiprows=3, names = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']) # clean up column names and first two rows
    return df, ticker