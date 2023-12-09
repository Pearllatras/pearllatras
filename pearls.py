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
lottie_coding = load_lottieurl("https://lottie.host/65dd4082-786e-45fc-b781-818d5fa0f6dc/PtqocH9wII.json")

# ---- HEADER SECTION ----
with st.container():
  st.subheader("Hi, I am Pearl :wave:")
  st.title("A Computer Engineering Student from SNSU")
  st.write("I am here to learn more about this amazing course with my co-student. And with the help of my instructure and also the tutorial on yt I made my own webpage with my own hard word and knowlegde.")
  
# ---- WHAT I DO ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What you need to know")
    st.write("##")
    st.write(
        """
       * I am Pearl Marie J. Latras
       * 18 years old born on the second day of April 2005
       * My both parents was a pure Filipino
       * My father was a  farmer and my mother was also a house wife
       * I have a 3 siblings and I am the 3rd one
       * I also love to draw, exploring new things specially when I can get some knowledge
        """
    )   
with right_column:
  st_lottie(lottie_coding, height=300, key="coding")
