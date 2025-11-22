import pandas as pd
import matplotlib.pyplot as plt
import get_goldPrice

"""
here we read data first and we want to do it
based on dates that is in the third row of our data
"""
df_raw = pd.read_csv("data/gold_price.csv",  header=None)

# start from row 3
df = df_raw.iloc[2:].copy()
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# delete the Nan rows
df = df.dropna()

df["Date"] = pd.to_datetime(df["Date"])
for col in ["Close", "High", "Low", "Open", "Volume"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.insert(1, "Change", df["Close"] - df["Open"])

print(df.head())
print(df.tail())
print(df.describe())


average_price = df["Close"].mean()
print(f"\nAverage Close Price: {average_price:.2f}")

print(f"Max price: {df['High'].max():.2f}")
print(f"Min price: {df['Low'].min():.2f}")

# adding the plot
plt.plot(df["Date"], df["Close"])
plt.xlabel("Dates")
plt.ylabel("Price")
plt.show()

# changes of price in the last 30 days
last_days_df = df.tail(30)

plt.bar(last_days_df["Date"], last_days_df["Change"], color=["green" if c > 0 else "red" for c in last_days_df["Change"]])
plt.xlabel("Dates")
plt.ylabel("Changes")
plt.show()





