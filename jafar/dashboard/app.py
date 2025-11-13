import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("Jafar Risk Dashboard")

# Risk Heatmap
symbols = ["AAPL", "MSFT", "GOOGL"]
risks = [requests.get(f"http://fastapi:8000/risk/{s}").json() for s in symbols]
df = pd.DataFrame(risks)
st.dataframe(df)

fig = px.heatmap(df[["jafar_risk"]], x=symbols, y=["Risk"], color_continuous_scale="reds")
st.plotly_chart(fig)

# Macro Outlook Panel
st.header("Macro Outlook")
macro = requests.get("http://fastapi:8000/macro/outlook").json()
st.gauge("Inflation (CPI)", value=macro["cpi"], min_value=0, max_value=10)
st.gauge("Rates (10Y)", value=macro.get("10y", 4.5), min_value=0, max_value=10)
st.gauge("VIX", value=macro["vix"], min_value=0, max_value=50)

# Sample query
st.text("What happens to tech if CPI > 4%? Higher risk due to tightening.")