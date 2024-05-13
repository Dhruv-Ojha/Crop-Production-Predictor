import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


st.title("CROP PRODUCTION PREDICTOR")
st.sidebar.title("Crop Production Predictor")

st.sidebar.markdown("This application is supposed to facilitate the local governments by predicting the crop production for the upcoming season. This will also help the farmers.")

DATA_URL1 = ("preprocessed_data_rabi.csv")

@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL1)
    return data

data = load_data()
if st.sidebar.checkbox("Show raw data", False):
    st.write(data)

st.sidebar.markdown("### Enter the year")
yr = st.sidebar.text_input("Crop")
filtered_data= data[data['Crops']==yr]
if not filtered_data.empty:
    st.write(filtered_data)
else:
    if yr != "":
        st.write("No data found for the given year")

dist_names = data["Dist Name"].unique()
crop_names = data["Crops"].unique()

# Create sidebar elements
selected_dist_name = st.sidebar.selectbox("Select District", dist_names)
selected_crop_name = st.sidebar.selectbox("Select Crop", crop_names)

# Filter data based on selections
filtered_data = data[
    (data["Dist Name"] == selected_dist_name) & (data["Crops"] == selected_crop_name)
]

# Plot line chart with plotly express
fig = px.line(filtered_data, x="Year", y=["Area", "Irrigation"], title="Irrigation & Area Trend")
st.plotly_chart(fig)

