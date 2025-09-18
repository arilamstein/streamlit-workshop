import streamlit as st
import pandas as pd

#st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

st.dataframe(df)
