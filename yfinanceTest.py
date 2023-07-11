import pandas as pd
import yfinance as yf
import streamlit as st
import streamlit_extras.altex as ste

# 銘柄を指定
ticker = ["7203.T", "AMZN", "AAPL"]

# 銘柄毎に株価を取得して
for tic in ticker :
    brand = yf.Ticker(tic)
    tmp = brand.history(period = "max")
    tmp.reset_index(inplace= True)
    tmp = tmp.rename(columns={'index':'Date'})
    tmp = tmp[['Date', 'Open']]
    tmp = tmp.assign(symbol=tic)
    if 'hist' in locals() :
        hist = pd.concat([hist, tmp], axis=0)
    else :
        hist = tmp


ste.line_chart(
    data=hist.query("symbol == 'AMZN'"),
    x="Date",
    y="Open",
    title="line chart",
)

ste.line_chart(
    data=hist,
    x="Date",
    y="Open",
    color="symbol",
    title="multi line chart",
)

ste.bar_chart(
    data=hist.query("symbol == 'AMZN'"),
    x="Date",
    y="Open",
    title="line chart",
)

left, middle, right = st.columns(3)
with left:
    data = hist.query("symbol == '7203.T'")
    st.metric("7203.T", int(data["Open"].mean()))
    ste.line_chart(
    data=data,
    x="Date",
    y="Open",
    title="line chart",
    )
with middle:
    data = hist.query("symbol == 'AMZN'")
    st.metric("AMZN", int(data["Open"].mean()))
    ste.line_chart(
    data=data,
    x="Date",
    y="Open",
    title="line chart",
    )
with right:
    data = hist.query("symbol == 'AAPL'")
    st.metric("AAPL", int(data["Open"].mean()))
    ste.line_chart(
    data=data,
    x="Date",
    y="Open",
    title="line chart",
    )