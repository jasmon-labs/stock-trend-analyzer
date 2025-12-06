
📈 Stock Price Trend Analyzer

A simple but serious Python project that pulls real stock market data and analyzes trends using popular technical indicators like SMA, EMA, RSI, and MACD.
Built to learn the fundamentals of market analysis, time-series patterns, and data visualization – and to show practical, project-ready Python skills.



🚀 What This Project Does

This tool helps you:
	•	Download historical stock prices
	•	Visualize short-term and long-term trends
	•	Calculate common indicators
	•	Identify potential buy/sell signals
	•	Generate charts for interpretation
	•	Build basic forecasting using regression
	•	Export charts/reports for quick analysis

It’s designed to be modular, readable, and easy to extend if you ever want to add backtesting, dashboards, or more indicators later.



🧩 Features

Technical Indicators
	•	SMA (Simple Moving Average) – short vs long trend
	•	EMA (Exponential Moving Average) – faster trend reaction
	•	RSI – checks overbought or oversold zones
	•	MACD – momentum & crossover signals

Visualizations
	•	Trend line charts
	•	RSI zone chart
	•	MACD crossover graph
	•	Candlestick chart (optional)

Extras
	•	CLI-style arguments for flexible usage
	•	Basic ML-based price forecasting
	•	Colorful terminal output (Rich)
	•	PDF report generation




📦 Installation

Clone the repo:

git clone https://github.com/jasmon-labs/stock-trend-analyzer
cd stock-trend-analyzer

Install requirements:

pip install -r requirements.txt




▶️ How to Run

Basic Run

python app.py

With Arguments

python app.py --ticker ^NSEI --period 6mo --indicators sma rsi macd --forecast --export pdf




🔍 Example Insights

The analyzer gives you:
	•	SMA crossover interpretation
	•	RSI zone warnings
	•	MACD momentum shift
	•	A short summary of the trend
	•	Optional 5-day forecast
	•	Exported charts in /charts/
	•	PDF report in /reports/



🛠 Tech Stack
	•	Python
	•	NumPy, Pandas (data handling)
	•	Matplotlib, Seaborn
	•	scikit-learn (forecasting)
	•	yfinance (data source)



🎯 Why I Built This

To build hands-on experience in finance + Python + data analysis.
Also wanted a proper GitHub-ready project that reflects:
	•	Structured coding
	•	Clean architecture
	•	Real market concepts
	•	Some ML exposure
	•	Practical visualization

This is a good starting point for anyone aiming at fintech, quantitative roles, or algo-trading basics.



✨ Future Improvements
	•	Backtesting engine
	•	Live dashboard (Streamlit)
	•	Strategy comparison
	•	Sentiment analysis using news APIs



🙋 Author

Jasmon
2nd-year Engineering Student • Fintech + Quant Curious • Learning Python & Market Analysis
