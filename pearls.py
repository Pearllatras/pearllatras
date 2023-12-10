from PIL import Image
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
img_contact_form = Image.open("images/pearl1.png")
img_lottie_animation = Image.open("images/pearl.png")

# ---- HEADER SECTION ----
with st.container():
  st.subheader("Hi, I am Pearl :wave:")
  st.title("A Computer Engineering Student from SNSU")
  st.write("I am here to learn more about this amazing course with my co-student.")

# ---- WHAT I DO ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What you need to know")
    st.write("##")
    st.write(
        """
        * I am Pearl Marie J. Latras 18 years old born on the second day of April 2005, 
          a BSCpE student of SNSU
          
          I am here to learn more about programming and how to create a website using python. 
          With the help of my instructure and the other website I create my own webpage with my own hard work
          
          As a student I quickly came here to understand that code is a superpower every young woman should be able to access.
          Code is going to containue to play a major role in defining our future
          
          Good software, like wine, takes time.
        """
    )
    
with right_column:
  st_lottie(lottie_coding, height=400, key="coding")
  # ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("W3School")
        st.write(
            """
            Learn how to create a program using Python!
          
            Python is a general-purpose language, meaning it can be used to create  a variety of 
            different programs and isn't specialized for any specific problem.
          
            In this website you can easliy learn how to create program using python.
            """
        )
        st.markdown("[Learn More...](https://www.w3schools.com/python/default.asp)")
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/platras@ssct.edu.ph" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
  
