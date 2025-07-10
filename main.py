
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Professional Trading Journal")
st.title("📈 Professional Trading Journal Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("data/pro_trading_journal_data.xlsx")

df = load_data()

st.subheader("Trade Summary")
st.dataframe(df, use_container_width=True)

st.subheader("Equity Curve")
df['Cumulative PnL'] = df['PnL'].cumsum()
st.line_chart(df.set_index("Date")['Cumulative PnL'])

st.subheader("Profit/Loss Distribution")
fig, ax = plt.subplots()
sns.histplot(df['PnL'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Win Rate")
win_rate = (df['PnL'] > 0).mean()
st.metric(label="Win Rate", value=f"{win_rate:.2%}")
