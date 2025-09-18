import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

state = st.selectbox("Select a State:", df["State"].unique())

mask = df["State"] == state
df_state = df[mask]

st.dataframe(df_state)
