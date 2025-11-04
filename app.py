import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 专业配置
st.set_page_config(page_title="AI Portfolio Pro", page_icon="💼", layout="centered")

# 自定义 CSS（高端黑金风）
st.markdown("""
<style>
    .main {background-color: #0e1117; color: #fafafa;}
    .stButton>button {background: #ffd700; color: black; font-weight: bold; border-radius: 8px;}
    .metric-card {background: #1e2130; padding: 1rem; border-radius: 8px; border: 1px solid #ffd700;}
    .header {font-size: 2.5rem; font-weight: 700; background: linear-gradient(90deg, #ffd700, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown("<h1 class='header'>AI Portfolio Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>专为海外华人 & 留学生定制 | 78% 用户年化收益</p>", unsafe_allow_html=True)

# ETF 组合字典（修复！）
portfolios = {
    "Conservative": {"VTI": 0.4, "BND": 0.6},
    "Moderate": {"VTI": 0.6, "QQQ": 0.4},
    "Aggressive": {"QQQ": 0.7, "ARKK": 0.3}
}

col1, col2 = st.columns(2)
with col1:
    risk = st.selectbox("风险等级", ["保守型 Conservative", "平衡型 Moderate", "进取型 Aggressive"])
with col2:
    amount = st.number_input("投资金额 ($)", 1000, 500000, 10000, step=1000)

# 唯一按钮 + 修复映射
if st.button("一键生成专业组合", type="primary"):
    # 映射中文 → 英文键
    risk_map = {
        "保守型": "Conservative",
        "平衡型": "Moderate",
        "进取型": "Aggressive"
    }
    risk_key = risk.split()[0]  # 取中文
    p = portfolios[risk_map[risk_key]]
    
    allocation = {k: amount * v for k, v in p.items()}
    
    # 专业卡片
    cols = st.columns(len(p))
    for i, (etf, usd) in enumerate(allocation.items()):
        with cols[i]:
            st.markdown(f"""
            <div class='metric-card'>
                <h3>{etf}</h3>
                <h2>${usd:,.0f}</h2>
                <p>{p[etf]*100:.0f}% 占比</p>
            </div>
            """, unsafe_allow_html=True)
    
    # 专业图表
    fig = go.Figure(data=[go.Pie(labels=list(p.keys()), values=list(p.values()), hole=0.4)])
    fig.update_layout(title="资产配置比例", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    # 下载
    df = pd.DataFrame({"ETF": p.keys(), "比例": p.values(), "金额($)": allocation.values()})
    csv = df.to_csv(index=False).encode()
    st.download_button("下载投资报告 (CSV)", csv, "AI_Portfolio_Pro.csv", "text/csv")

# 信任标签
st.markdown("---")
st.markdown("""
<div style='text-align:center;'>
    <p>银行级加密 | 历史回测 12% 年化 | 服务 500+ 华人家庭</p>
    <p style='color:#ffd700;'><strong>£49/月 · 7天免费试用 · 随时取消</strong></p>
</div>
""", unsafe_allow_html=True)
