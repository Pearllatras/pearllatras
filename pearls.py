import streamlit as st
st.set_pge_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
with st.container():
  st.subheader("Hi, I am Pearl :wave:")
  st.title("A Computer Engineering Student from SNSU")
  st.write("I am passionate to learn more about this amazing course")

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
    
