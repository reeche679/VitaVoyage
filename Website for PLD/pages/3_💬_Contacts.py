import streamlit as st
from PIL import Image

with st.container():
    st.subheader("CEO: Richmond S. Lingal")



expander = st.expander("Details")


expander.write("Richmonds")
Image = Image.open('Screenshot 2023-11-20 133016.png')
expander.image(Image)

