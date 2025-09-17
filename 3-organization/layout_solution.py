import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

col1, col2, col3 = st.columns(3)
with col1:
    state = st.selectbox("State:", df["State"].unique())
with col2:
    demographic = st.selectbox(
        "Demographic:", ["Total Population", "Median Household Income"]
    )
with col3:
    year = st.selectbox("Year:", df["Year"].unique())

graph_tab, map_tab, table_tab = st.tabs(["📈 Graph", "🗺️ Map", "📊 Table"])
with graph_tab:
    # State line graph
    mask = df["State"] == state
    df_state = df[mask]
    fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
    st.plotly_chart(fig)
with map_tab:
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
with table_tab:
    # All data for cmopleteness
    st.dataframe(df)
