import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


ticker = input("Enter stock ticker ")
period = input("Enter the period (1mo, 3mo, 6mo, 1y, 5y) ")
df = yf.download(ticker, period=period)
print(df.head())

df = df[['Open','High','Low','Close','Volume']]
df.dropna(inplace=True)

df['SMA20'] = df['Close'].rolling(20).mean()
df['SMA50'] = df['Close'].rolling(50).mean()
df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()

delta = df['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

exp1 = df['Close'].ewm(span=12, adjust=False).mean()
exp2 = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = exp1 - exp2
df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Close'], label="Close")
plt.plot(df['SMA20'], label="SMA20")
plt.plot(df['SMA50'], label="SMA50")
plt.title(f"{ticker} Price Trend")
plt.legend()
plt.grid()
plt.savefig(f"charts/{ticker}_trend.png")
plt.show()

plt.figure(figsize=(12,3))
plt.plot(df['RSI'], label="RSI")
plt.axhline(30, color='green')
plt.axhline(70, color='red')
plt.legend()
plt.savefig(f"charts/{ticker}_rsi.png")
plt.show()

df['Signal'] = 0
df['Signal'] = np.where(df['SMA20'] > df['SMA50'], 1, 0)
df['Positions'] = df['Signal'].diff()

plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close')

buy = df[df['Positions'] == 1]
sell = df[df['Positions'] == -1]

plt.scatter(buy.index, buy['Close'], marker='^', color='green', s=100)
plt.scatter(sell.index, sell['Close'], marker='v', color='red', s=100)

plt.title("Buy/Sell Signals")
plt.legend()
plt.savefig(f"charts/{ticker}_signals.png")
plt.show()

def generate_summary(df):
    sma20 = df['SMA20'].iloc[-1]
    sma50 = df['SMA50'].iloc[-1]
    rsi = df['RSI'].iloc[-1]

    trend = "uptrend" if sma20 > sma50 else "downtrend"
    rsi_status = "overbought" if rsi > 70 else "oversold" if rsi < 30 else "neutral"

    summary = f"""
    Current Trend: {trend}
    RSI Status: {rsi_status}
    20-day SMA: {round(sma20,2)}
    50-day SMA: {round(sma50,2)}
    """
    return summary

print(generate_summary(df))

df['Index'] = np.arange(len(df))
X = df[['Index']]
y = df['Close']

model = LinearRegression()
model.fit(X, y)

future_index = np.arange(len(df), len(df) + 5).reshape(-1, 1)
pred = model.predict(future_index)

print("Next 5-day predicted prices:")
print(pred)

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

summary = generate_summary(df)
pdf.multi_cell(0, 10, summary)

pdf.output(f"reports/{ticker}_report.pdf")