import streamlit as st
from PIL import Image
import base64
st.set_page_config(page_title="Welcome to VitaVoyage!", page_icon="logo.png", layout="wide", initial_sidebar_state="collapsed")

#Navbar
def create_navigation_bar():
    navigation_bar = f"""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" id="topNav" style="background-color: #112d32;">
       <a class="navbar-brand" href="http://localhost:8501/" target="_blank" style="padding-left: 60px;">VitaVoyage</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:8501/Get_Started" target="_blank">Get Started</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:8501/Contacts" target="_blank">Contacts</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:8501/Learn_More" target="_blank">Learn More</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://docs.google.com/document/d/12U7TMhvAxqI2LxrBNXZQ2JOEFgy1PLOZplDoF548a7U/edit" target="_blank">References</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://github.com/reeche679/VitaVoyage" target="_blank">Github Page</a>
          </li>
        </ul>
      </div>
    </nav>
    """
    st.markdown(navigation_bar, unsafe_allow_html=True)
    

# Call the function to create the navigation bar
create_navigation_bar()

def set_page_background_image(image_file):
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64(image_file)

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function with the image file path
set_page_background_image("C:/Users/PC/Desktop/Website for PLD/homepage background.jpg") 


# Header 
with open("C:/Users/PC/Desktop/Website for PLD/style/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
path = "C:/Users/PC/Desktop/Website for PLD/logo.png"
image = Image.open(path)



with st.container():
   st.markdown("""
<style>
.centered-text {
    font-family: 'Oswald', Oswald !important;
    font-size: 50px !important;
    text-align: center !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="centered-text">BE THE BEST VERSION OF YOURSELF</p>', unsafe_allow_html=True)

st.markdown("""
<style>
.centered-text1 {
    font-family: 'Poppins Light', sans-serif !important;
    font-size: 20px !important;
    text-align: center !important;
    color: white !important;
}
.divider {
    border-top: 4px solid white;
    margin: 20px auto;
    width: 20%;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="divider"></p>', unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.markdown('<p class="centered-text1">Elevate Your Journey.</p>', unsafe_allow_html=True)


# Bootstrap CSS link
st.markdown(
    """
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    """,
    unsafe_allow_html=True
)

# Centered Bootstrap button as a bigger yellow hyperlink
st.markdown(
    """
    <div class="d-flex justify-content-center">
        <a href="http://localhost:8501/Get_Started" class="btn btn-warning btn-lg" style="color: white; border-color: black;">Click Here to Get Started</a>
    </div>
    """,
    unsafe_allow_html=True
)

#--- About VitaVoyage ---#
from subprocess import check_output


