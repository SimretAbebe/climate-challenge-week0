import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_all_data


st.set_page_config(page_title="Africa Climate Dashboard", layout="wide", page_icon="")


st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1, h2, h3, p, span, label { color: white !important; }
    [data-testid="stMetric"] { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)


df = load_all_data()
st.sidebar.title("Mission Control")
selected_countries = st.sidebar.multiselect("Select Regions", df['Country'].unique(), default=df['Country'].unique())
year_range = st.sidebar.slider("Analysis Period", int(df['Year'].min()), int(df['Year'].max()), (2015, 2026))
f_df = df[(df['Country'].isin(selected_countries)) & (df['Year'].between(year_range[0], year_range[1]))]


st.title("Africa Climate Resilience Dashboard")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Avg Temp", f"{f_df['T2M'].mean():.1f}°C")
m2.metric("Max Temp", f"{f_df['T2M_MAX'].max():.1f}°C")
m3.metric("Avg Daily Rain", f"{f_df['PRECTOTCORR'].mean():.2f}mm")
m4.metric("Days Analyzed", f"{len(f_df):,}")
st.divider()


c1, c2 = st.columns(2)

with c1:
    st.subheader("Temperature Trends")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    plot_df = f_df.groupby(['Country', pd.Grouper(key='Date', freq='MS')])['T2M'].mean().reset_index()
    sns.lineplot(data=plot_df, x='Date', y='T2M', hue='Country', ax=ax1, linewidth=2.5, palette="bright")
    ax1.set_facecolor('#161b22')
    fig1.patch.set_facecolor('#0e1117')
    ax1.tick_params(colors='white')
    st.pyplot(fig1)

with c2:
    st.subheader("Precipitation Variability")
    
    
    sns.set_style("whitegrid")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    
    sns.boxplot(data=f_df, x='Country', y='PRECTOTCORR', hue='Country', ax=ax2, palette="viridis", legend=False)
    

    ax2.set_title("Daily Precipitation Variability Comparison (2015-2026)", fontsize=14, color='black')
    ax2.set_ylabel("Precipitation (mm/day)", color='black')
    ax2.set_xlabel("Country", color='black')
    ax2.tick_params(colors='black')
    
    st.pyplot(fig2)
    
    
    sns.reset_orig()


with st.expander("Inspect Raw Data Sample"):
    st.dataframe(f_df.sample(min(100, len(f_df))), use_container_width=True)
