# imports
import streamlit as st
import cv2
import csv
from PIL import Image
import pandas as pd
import time
import os
import numpy as np
from datetime import time
from search_word import search_word


# sidebar
st.sidebar.image("../assets/logo.png")
st.sidebar.header("Search Module")
st.sidebar.markdown(
    "Utilizing data analytics and data algorithms, we provide a light yet efficient search and data analyzer for the **_'cap-bot'_** predicitons while ensuring a safe and convenient environment to aid the search"
)
st.sidebar.header("Features")
st.sidebar.markdown("""- Get a visualization of the CCTV Cameras""")
st.sidebar.markdown("""- Define keywords of the event""")
st.sidebar.markdown("""- Define time of the event""")
st.sidebar.markdown("[Github Repository](https://github.com/aryankargwal/capbot2.0)")
st.sidebar.markdown("[Proposal Video](https://www.youtube.com/watch?v=Sr8dNQMBRZI)")


# Data Uploads
st.header("Data Uploading")
# uploading results
st.subheader("Upload the CCTV Log here")
file = st.file_uploader("logs")


# loading results
@st.cache
def load_data(nrows):
    data = pd.read_csv(file, nrows=nrows)
    lower = lambda x: str(x).lower()
    data.rename(lower, axis="columns", inplace=True)
    return data


if file is not None:
    data_load_state = st.text("")
    data = load_data(10000)
    # seeing data
    st.subheader("Raw data")
    st.write(data)

# sample cctv map
st.subheader("Upload the CCTV Co-ordinates here")
cctv_map = st.file_uploader("co-ordinates")
if cctv_map is not None:
    st.subheader("CCTV Map")
    df = pd.read_csv(cctv_map)
    st.map(df)


# Search
st.header("Searching Logs")

# keywords
st.subheader("Enter the keywords of the incident")
keywords = st.text_input("")
keywords = keywords.split(sep=" ")
list(keywords)

# time
st.subheader("The time where the incident might have occured")
footage_time = st.slider("", value=(time(9, 30), time(14, 45)))
# button
if st.button("Start Search"):
    row = search_word(data, keywords)
    for k in row:
        st.write(data.loc[[k], :])
