import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_streamlit = load_lottiefile("./Streamlit Logo Animation.json")
st.lottie(lottie_streamlit, height=400, key="initial")