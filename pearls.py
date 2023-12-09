import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

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
  
