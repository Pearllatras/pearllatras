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
lottie_coding = load_lottieurl("https://lottie.host/f55fae42-4cd9-410b-8be2-911c8823610e/L8JGXaVJsA.json")

# ---- HEADER SECTION ----
with st.container():
  st.subheader("Hi, I am Pearl :wave:")
  st.title("A Computer Engineering Student from SNSU")
  st.write("I am here to learn more about this amazing course with my co-student")

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
       * EXPLORING ABOUT NEW THINGS
        """
    )   
with right_column:
  st_lottie(lottie_coding, height=400, key="coding")
