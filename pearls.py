import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
 if r.status_code != 200:
   return None
  return r.json()

# ---- LOAD ASSETS ----
Lottie_coding= load_lottieurl("https://app.lottiefiles.com/animation/571d91e8-a4f0-4f44-9176-da69a0cdb146")

# ---- HEADER SECTION ----
with st.container():
  st.subheader("Hi, I am Pearl :wave:")
  st.title("A Computer Engineering Student from SNSU")
  st.write("I am passionate to learn more about this amazing course")

# ---- WHAT I DO ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I like")
    st.write("##")
    st.write(
        """
       * DRAWING
       * WATCHING ANIME/KDRAMAS
       * SWIMMING
       * ROAD TRIP/ISLAND HOPPING
        """
    )
    st.write("My Github Account >](https://github.com/Pearllatras/pearllatras/edit/main/pearls.py")
    with rigth_column
    st.lottie(lottie_coding, height=400, key="coding")
