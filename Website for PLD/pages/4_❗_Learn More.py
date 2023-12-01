import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from Homepage import create_navigation_bar, set_page_background_image


# Page Config
st.set_page_config(page_title="Learn More", page_icon = "logo.png" ,initial_sidebar_state="collapsed")
  


# Navigation Bar

create_navigation_bar()
st.markdown(
    """
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    """,
    unsafe_allow_html=True)
    


#---- Header ----#

with open("style\style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
path = "logo.png"
image = Image.open(path)


selected = option_menu(
    menu_title=None,
    options=["Objectives", "Mission", "Vision"],
    icons=["check", "envelope", "eye"],
    default_index=0,
    orientation="horizontal"
  )
st.markdown("""
<style>
.centered-text {
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
    font-style: italic;
    font-family: Poppins Light;
}
</style>
""", unsafe_allow_html=True)

if selected == "Objectives":
    st.markdown("""
<style>
.centered-header1 {
    text-align: center;
    color: white;
    font-size: 50px;
    font-weight: bold;
    font-family: Oswald;
}
</style>
""", unsafe_allow_html=True)
    st.markdown('<h1 class="centered-header1">Our Objective</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="centered-text">"Revolutionizing Health: Crafting a Stronger You Through Personalized Fitness and Nourishing Meal Experiences."</h1>', unsafe_allow_html=True)

if selected == "Mission":
    st.markdown("""
<style>
.centered-header1 {
    text-align: center;
    color: white;
    font-size: 50px;
    font-weight: bold;
    font-family: Oswald;
}
</style>
""", unsafe_allow_html=True)
    st.markdown("""
""", unsafe_allow_html=True)
    st.markdown('<h1 class="centered-header1">Our Mission</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="centered-text">"Empowering lives through fitness, fostering strength, and inspiring resilience for a healthier, happier world."</h1>', unsafe_allow_html=True)
    
if selected == "Vision":
    st.markdown("""
<style>
.centered-header1 {
    text-align: center;
    color: white;
    font-size: 50px;
    font-weight: bold;
    font-family: Oswald;
}
</style>
""", unsafe_allow_html=True)
    st.markdown("""
""", unsafe_allow_html=True)
    st.markdown('<h1 class="centered-header1">Our Vision</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="centered-text">"Envisioning a world where every individual embraces a fit and vibrant lifestyle, unlocking their full potential for a life of vitality and well-being."</h1>', unsafe_allow_html=True)
    


set_page_background_image("learn more background.jpg")


