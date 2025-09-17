import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

# UI Options
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Hi! I'm column 1!")
with col2:
    st.write("And I'm column 2.")
with col3:
    st.write("Saved the best for last.")

state = st.selectbox("Select a State:", df["State"].unique())
demographic = st.selectbox(
    "Select a Demographic:", ["Total Population", "Median Household Income"]
)
year = st.selectbox("Select a Year:", df["Year"].unique())

# State line graph
mask = df["State"] == state
df_state = df[mask]
fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
st.plotly_chart(fig)

# Map for year
mask = df["Year"] == year
df_year = df[mask]

fig = px.choropleth(
    df_year,
    locations="State Abbrev",  # Column for region
    locationmode="USA-states",
    color=demographic,  # Column for color
    scope="usa",
    title=f"{demographic} for {year}",
)
st.plotly_chart(fig)

# All data for cmopleteness
st.dataframe(df)
