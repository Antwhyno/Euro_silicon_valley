import streamlit as st

def show_page():
    # Pour afficher l'image correspondante
    st.image("images/Slide4.jpg", caption=" ", use_container_width=True)

    st.link_button("map", "https://www.siliconvalleymap.org/")