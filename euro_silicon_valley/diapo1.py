import streamlit as st

def show_page():
    st.header("Diapositive 1")
    
    # Pour afficher l'image
    st.image("images/Slide1.jpg", caption=" ", use_container_width=True)
    
    st.write("Ceci est le contenu de la diapositive 1.")
