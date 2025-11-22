import yfinance as yf
import pandas as pd
from datetime import date

today = date.today().strftime("%Y-%m-%d")

data = yf.download("GC=F", start="2024-01-01", end=today)

data.to_csv("data/gold_price.csv")

print("gold price saved to gold_price.csv file.")