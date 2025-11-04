import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="AI Portfolio Builder", page_icon="📈")

st.title("📈 AI Portfolio Builder")
st.markdown("### For Overseas Chinese & Students")

col1, col2 = st.columns(2)
with col1:
    risk = st.selectbox("Risk Level", ["Conservative", "Moderate", "Aggressive"])
with col2:
    amount = st.number_input("Investment ($)", 1000, 100000, 10000)

portfolios = {
    "Conservative": {"VTI": 0.4, "BND": 0.6},
    "Moderate": {"VTI": 0.6, "QQQ": 0.4},
    "Aggressive": {"QQQ": 0.7, "ARKK": 0.3}
}

if st.button("🚀 Generate Portfolio"):
    p = portfolios[risk]
    allocation = {k: amount * v for k, v in p.items()}
    
    st.success(f"✅ {risk} Portfolio")
    for etf, usd in allocation.items():
        st.metric(etf, f"${usd:,.0f}")
    
    data = pd.DataFrame(p, index=["Weight"]).T
    st.bar_chart(data)
    
    csv = data.to_csv().encode()
    st.download_button("Download CSV", csv, "portfolio.csv", "text/csv")
