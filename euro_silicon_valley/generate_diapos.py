import os

template = """import streamlit as st

def show_page():
    st.header("Diapositive {num}")
    
    # Pour afficher l'image correspondante
    st.image("images/Slide{num}.jpg", caption=" ", use_container_width=True)
"""

for i in range(1, 23):
    with open(f"diapo{i}.py", "w", encoding="utf-8") as f:
        f.write(template.format(num=i))

print("Les 22 diapositives ont été générées avec succès (avec images centrées sans texte).")
