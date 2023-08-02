import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_streamlit = load_lottiefile("./Streamlit Logo Animation.json")
lottie_progress_url = "https://assets5.lottiefiles.com/private_files/lf30_3ykigvxc.json"
lottie_progress = load_lottieurl(lottie_progress_url)

with st.sidebar:
    speed = st.slider("Select speed", 0.1, 2.0, 1.0)
    reverse = st.checkbox("Reverse direction", False)
st.lottie(lottie_streamlit, speed=speed, reverse=reverse, height=400, key="initial")