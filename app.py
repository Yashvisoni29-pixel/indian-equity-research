python
import streamlit as st
import yfinance as yf
import pandas as pd
st.set_page_config(page_title="indian equity research",layout="wide")
st.title("indian equity research dashboard")
st.subheader("stock market analysis & performance")
st.write("analyze indian listed companies using market data.")
ticker = st.text_input("enter NSE stock symbol","RELIANCE.NS")
Period = st. selectbox("select analysis period",["1mo","3mo","6mo","1y","2y","5y"], index =3)
if st.button("analyze stock"):
  with st.spinner("fetching stock market data..."):
    stock = yf ticker (ticker.strip().upper())
    data = stock.history(period=period)
  if data.empty:
    st.error("no data found. check the stock symbol.")
  else:
    data = data.dropna( subnet=["close"])
    latest = float(data["close"].iloc[-1])
    previous = (
      float(data
    import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Indian Equity Research", layout="wide")
st.title("Indian Equity Research Dashboard")
st.subheader("Stock Market Analysis & Performance")
st.write("Analyze Indian listed companies using market data.")

ticker = st.text_input("Enter NSE Stock Symbol", "RELIANCE.NS")
period = st.selectbox("Select Analysis Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

if st.button("Analyze Stock"):
    with st.spinner("Fetching stock market data..."):
        stock = yf.Ticker(ticker.strip().upper())
        data = stock.history(period=period)

    if data.empty:
        st.error("No data found. Check the stock symbol.")
    else:
        data = data.dropna(subset=["Close"])
        latest = float(data["Close"].iloc[-1])
        previous = float(data["Close"].iloc[-2]) if len(data) > 1 else latest
        daily_change = ((latest / previous) - 1) * 100 if previous else 0
        total_return = ((latest / float(data["Close"].iloc[0])) - 1) * 100
        returns = data["Close"].pct_change().dropna()
        volatility = returns.std() * (252 ** 0.5) * 100 if len(returns) > 1 else 0

        st.success("Analysis completed!")
        st.write("Latest available trading date:", str(data.index[-1].date()))
        col1, col2, col3 = st.columns(3)
        col1.metric("Latest Closing Price", f"₹{latest:,.2f}", f"{daily_change:+.2f}%")
        col2.metric("Period Return", f"{total_return:.2f}%")
        col3.metric("Annualized Volatility", f"{volatility:.2f}%")

        data["20 Day Average"] = data["Close"].rolling(20).mean()
        data["50 Day Average"] = data["Close"].rolling(50).mean()
        st.subheader("Stock Price Trend")
        st.line_chart(data[["Close", "20 Day Average", "50 Day Average"]])
        st.subheader("Historical Market Data")
        st.dataframe(data.tail(10), use_container_width=True)
        st.caption("Source: Yahoo Finance via yfinance. Data may be delayed and is not guaranteed to be real-time.")

st.divider()
st.caption("Educational financial research project. Not investment advice.")
