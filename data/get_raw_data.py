import yfinance as yf
from datetime import datetime


def get_data(file_path, ticker="ENI.MI", start="2020-01-01", end=None):
    # Gets data from Yahoo Finance and saves it
    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')
    print(f"Getting data for {ticker} from {start} to {end}...")
    data = yf.download(ticker, start=start, end=end) # Download
    data.to_csv(file_path) # Save
    print(f"CSV file saved to: {file_path}")
    return ticker