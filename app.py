import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_streamlit = load_lottiefile("./Streamlit Logo Animation.json")
with st.sidebar:
    speed = 1
    reverse = False
st.lottie(lottie_streamlit, speed=speed, reverse=reverse, height=400, key="initial")