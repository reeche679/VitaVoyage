import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# Set page configuration
img_path = "logo.png"
img = Image.open(img_path)
st.set_page_config(page_title="VitaVoyage!", page_icon=img, layout="wide", initial_sidebar_state="collapsed")



# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load Animation
animation_symbol = "❄"
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

# Load Bootstrap CSS
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

# Navigation Bar
st.markdown(f"""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark justify-content-center" id="topNav" style="background-color: #a83232;">
  <a class="navbar-brand" href="#" target="_blank">
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ms-auto">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#"><span class="mx-auto">Home</span> <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8501/Get_Started" target="_blank"><span class="mx-auto">Get Started</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8501/References" target="_blank"><span class="mx-auto">References</span></a>
            <li class="nav-item">
        <a class="nav-link" href="http://localhost:8501/Get_Started" target="_blank"><span class="mx-auto">Contacts</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8501/References" target="_blank"><span class="mx-auto">Github Page</span></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Header
with st.container():
    st.title("Welcome to VitaVoyage!")
    st.subheader("Your personal health adventure!")
    st.write("Doctors? Who needs those! Using VitaVoyage, make all your healthcare accessible within a single site! 🥶 (Get a doctor for serious cases though)")

# Sidebar
logo_url = 'logo.png'
st.sidebar.image(logo_url)
selected = option_menu(
    menu_title=None,
    options=["Objectives", "References"],
    menu_icon="cast",
    icons=["check-circle-fill", "book-fill"],
    orientation="horizontal",
)

if selected == "Objectives":
    st.write("Insert objectives here")
st.sidebar.success("Select a page.")
if selected == "References":
    st.write("Insert references here")

# About VitaVoyage
from subprocess import check_output