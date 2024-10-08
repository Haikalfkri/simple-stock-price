import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Apple!         
""")

# define the ticker symbol
tickerDymbol = 'AAPL' # ticker symbol for apple
# get data on this ticker
tickerData = yf.Ticker(tickerDymbol)
# get historical price for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)