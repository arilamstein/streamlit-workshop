import pandas as pd
import plotly.express as px


def get_data():
    return pd.read_csv("state_data.csv")


def get_unique_states():
    df = get_data()
    return df["State"].unique()


def get_unique_years():
    df = get_data()
    return df["Year"].unique()


def get_line_graph(state, demographic):
    df = get_data()

    mask = df["State"] == state
    df_state = df[mask]

    return px.line(
        df_state, x="Year", y=demographic, title=f"{demographic} for {state}"
    )


def get_map(demographic, year):
    df = get_data()

    mask = df["Year"] == year
    df_year = df[mask]

    return px.choropleth(
        df_year,
        locations="State Abbrev",  # Column for region
        locationmode="USA-states",
        color=demographic,  # Column for color
        scope="usa",
        color_continuous_scale="Viridis",
        title=f"{demographic} for {year}",
    )
