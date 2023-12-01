import streamlit as st
from PIL import Image
import plotly.express as px
from Homepage import set_page_background_image, create_navigation_bar

# Page Config
st.set_page_config(page_title="Contacts", page_icon = "logo.png" , initial_sidebar_state="collapsed")

# Background Image
set_page_background_image("meet-the-team-title-background-v2.jpg")
  
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

st.markdown("""
<style>
.divider {
    border-top: 2px solid white;
    margin: 10px auto;
    width: 200%;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.divider2 {
    border-top: 2px solid white;
    margin: 30px auto;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-family: Forum; text-align: center; font-size: 5em; font-weight: bold;"> VitaVoyage: <br>Meet the Team</p>', unsafe_allow_html=True)
st.markdown('##')

_, col2, _ = st.columns([1, 2, 1])
with col2:
        st.markdown('##')

_, image_column, text_column = st.columns((1, 2, 3))
    
with image_column:
        image = Image.open('Images/rich.jpg')
        st.image(image, width=180)
        st.write(" ")
        image = Image.open('Images/jorgette.jpg')
        st.write(" ")
        st.image(image, width=180)
        st.write(" ")
        image = Image.open('Images/joriel.jpg')
        st.write(" ")
        st.image(image, width=180)
        st.write(" ")
        image = Image.open('Images/kyle.jpg')
        st.write(" ")
        st.image(image, width=180)
        st.write(" ")
        st.write(" ")
        image = Image.open('Images/clarence.jpg')
        st.image(image, width=180)
    

    
with text_column:
    st.markdown("<p style='color:white; font-size:30px;'> <strong>Team Leader  ‎ ‎ ‎ ‎ ‎ ‎ ‎  </strong>     Richmond S. Lingal </p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Email : lingalrichmond74@gmail.com</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Contact Number : 0916-289-3614</p>", unsafe_allow_html=True)
#Divider    
   
    st.markdown('<p class="divider"></p>', unsafe_allow_html=True)

#End of Divider
    #Aira
    st.markdown("<p style='color:white; font-size:30px;'><strong>Senior Associate ‎ ‎ ‎ ‎</strong> Jorgette Aira M. Amaro  </p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Email : jorgetteairaamaro@gamil.com</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Contact Number : 0947-584-7075</p>", unsafe_allow_html=True)
    st.write("")
    st.markdown('<p class="divider"></p>', unsafe_allow_html=True)
    
    #Joriel
    st.markdown("<p style='color:white; font-size:30px;'><strong>Junior Associate ‎ ‎ ‎ ‎ </strong> ‎ ‎ ‎ ‎ ‎ Joriel Laurence S. Singh  </p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Email : jorielsingh0820@gmail.com</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Contact Number : 0948-570-7761</p>", unsafe_allow_html=True)
    st.write("")
    st.markdown('<p class="divider"></p>', unsafe_allow_html=True)
    #Kyle
    st.markdown("<p style='color:white; font-size:30px;'><strong>Contributor‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎</strong>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Kyle Dranmay Dalangin </p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Email : dranmaykyle06@gmail.com</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Contact Number : 09465684105</p>", unsafe_allow_html=True)
    st.write("")
    st.markdown('<p class="divider"></p>', unsafe_allow_html=True)  
    #Clarence
    st.markdown("<p style='color:white; font-size:30px;'><strong>Contributor‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎</strong>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Clarence Adrian M. Caraig </p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Email : clarence.caraig26@gmail.com </p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Contact Number : 09564770779</p>", unsafe_allow_html=True)
    st.write(" ")
    st.markdown('<p class="divider"></p>', unsafe_allow_html=True)

    

