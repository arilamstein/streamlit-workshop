import streamlit as st
import backend as be

st.title("Explore US Census Data")

col1, col2, col3 = st.columns(3)
with col1:
    state = st.selectbox("State:", be.get_unique_states())
with col2:
    demographic = st.selectbox(
        "Demographic:", ["Total Population", "Median Household Income"]
    )
with col3:
    year = st.selectbox("Year:", be.get_unique_years())

graph_tab, map_tab, table_tab = st.tabs(["📈 Graph", "🗺️ Map", "📊 Table"])
with graph_tab:
    fig = be.get_line_graph(state, demographic)
    st.plotly_chart(fig)
with map_tab:
    fig = be.get_map(demographic, year)
    st.plotly_chart(fig)
with table_tab:
    df = be.get_data()
    st.dataframe(df)
