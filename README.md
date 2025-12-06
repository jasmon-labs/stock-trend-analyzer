📈 Stock Price Trend Analyzer

A full-featured stock market analysis project built using Python, designed to analyze price trends, generate indicators (SMA, EMA, RSI, MACD), create buy/sell signals, perform forecasting, and auto-generate visual reports.

This project is perfect for quantitative analysis, algo-trading basics, and resume-ready financial engineering exposure.


🚀 Features

📊 Technical Indicators
	•	Simple Moving Average (SMA 20, 50)
	•	Exponential Moving Average (EMA)
	•	RSI (Relative Strength Index)
	•	MACD + Signal Line

📈 Trend Visualizations
	•	Price vs SMA/EMA
	•	RSI Chart
	•	MACD Chart
	•	Candlestick Chart (Plotly)

💡 Smart Insights

Automatic interpretation of:
	•	Trend (Uptrend / Downtrend)
	•	Momentum
	•	Overbought / Oversold zones
	•	MACD crossover signals

🧠 Forecasting (Machine Learning)
	•	Linear regression 5-day price prediction
	•	Forecast chart

💼 Buy/Sell Signal Generator

Based on:
	•	SMA crossover strategy
	•	Momentum confirmation
	•	RSI conditions

📑 PDF Report Generation
	•	Summary
	•	Indicators
	•	Charts
	•	Forecasts

🌐 Modular Architecture

Clean, professional structure:

indicators/   → All indicator math
plots/        → Chart generators
models/       → ML forecasting
utils/        → Data loading
charts/       → Auto-generated images
reports/      → PDF outputs

🛠 CLI Support (Command Line Usage)

Example:

python app.py --ticker TCS.NS --period 1y --export pdf --forecast


⸻

🏗 Project Structure

stock-trend-analyzer/
│
├── app.py                   # Main application file
├── requirements.txt         # Project dependencies
├── README.md                # Documentation
│
├── indicators/
│   ├── sma.py               # Simple Moving Average
│   ├── ema.py               # Exponential Moving Average
│   ├── rsi.py               # RSI implementation
│   ├── macd.py              # MACD logic
│
├── plots/
│   ├── trend_plot.py        # Price + SMA plot
│   ├── rsi_plot.py          # RSI chart
│   ├── macd_plot.py         # MACD chart
│
├── models/
│   └── forecast.py          # Linear Regression forecasting
│
├── utils/
│   └── data_loader.py       # YFinance download & cleaning
│
├── charts/                  # Generated images
└── reports/                 # Auto-generated PDF reports


⸻

🧩 Dependencies

Install everything using:

pip install -r requirements.txt

requirements.txt

yfinance
numpy
pandas
matplotlib
seaborn
scikit-learn
fpdf
loguru
plotly
rich


▶- How to Run

Basic usage:

python app.py

Advanced usage (CLI):

python app.py --ticker ^NSEI --period 1y --indicators sma rsi macd --forecast --export pdf



🤖 Example Output
	•	Trend Analysis Chart
	•	RSI + Overbought/Oversold levels
	•	MACD crossover analysis
	•	Buy/Sell markers
	•	5-day forecast
	•	Auto-generated PDF report



📌 Why This Project Matters

This tool showcases your skills in:
	•	Financial market data analysis
	•	Python data science ecosystem
	•	Time-series analysis
	•	Machine learning (basic forecasting)
	•	Visualization
	•	Modular software design
	•	CLI app development
	•	Report generation

Perfect for roles in:
	•	Finance / Quant
	•	Data Analytics
	•	Software Engineering
	•	Machine Learning



🧑‍💻 Author

Jasmon
2nd-year Engineering Student passionate about fintech, algo trading, and quantitative analysis.

