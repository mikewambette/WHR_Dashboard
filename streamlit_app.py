import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("WHR2023.CSV", sep=";")

df = load_data()

st.title("World Happiness Report Dashboard")

years = sorted(df["year"].unique())
selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)

data_year = df[df["year"] == selected_year]
st.subheader(f"Top 10 Countries by Life Ladder in {selected_year}")
top10 = data_year.nlargest(10, "Life Ladder")[["Country name", "Life Ladder"]]
st.bar_chart(top10.set_index("Country name"))

st.subheader("Summary Statistics")
st.dataframe(data_year.describe())