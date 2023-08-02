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
lottie_success_url = "https://assets7.lottiefiles.com/packages/lf20_TsKMbf.json"
lottie_error_url = "https://assets6.lottiefiles.com/packages/lf20_0pgmwzt3.json"

st.set_page_config(
    page_icon=":tada:",
    initial_sidebar_state="collapsed",
)


with st.sidebar:
    st.header("Animation parameters")
    speed = st.slider("Select speed", 0.1, 2.0, 1.0)
    reverse = st.checkbox("Reverse direction", False)
st.lottie(lottie_streamlit, speed=speed, reverse=reverse, height=400, key="initial")

with st.sidebar:
    st.markdown(
        '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
        unsafe_allow_html=True,
    )

c_col1, colx, c_col2, coly = st.columns((1, 0.1, 0.25, 1))
if c_col1.button("Run some heavy computation...for 5 seconds!"):
    with c_col2.empty():
        with st_lottie_spinner(lottie_progress, loop=True, key="progress"):
            time.sleep(5)
        st_lottie(lottie_success_url, loop=False, key="success")