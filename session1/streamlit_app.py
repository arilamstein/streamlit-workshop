import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_data.csv")

st.header("US State Demographics")

# Let user select which state to graph
state = st.selectbox("State:", df["State"].unique())

# Create a graph of total population
df_state = df[df["State"] == state]
fig = px.line(
    df_state, x="Year", y="Total Population", title=f"Total Population of {state}"
)
st.plotly_chart(fig)

# Show the entire dataframe
st.write("All Data")
st.dataframe(df)
