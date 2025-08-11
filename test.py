import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "GOOGL"]

data = yf.download(tickers, start="2023-01-01", end="2023-12-31")

# Just use 'Close' since 'Adj Close' is gone when auto_adjust=True
close_prices = data["Close"]
print(close_prices.head())
