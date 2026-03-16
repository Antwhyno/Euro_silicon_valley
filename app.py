import streamlit as st
import streamlit.components.v1 as components

# Importation de toutes les diapos
import diapo1, diapo2, diapo3, diapo4, diapo5, diapo6, diapo7, diapo8, diapo9, diapo10
import diapo11, diapo12, diapo13, diapo14, diapo15, diapo16, diapo17, diapo18, diapo19, diapo20
import diapo21, diapo22

# Configuration
st.set_page_config(page_title="Euro Silicon Valley - Présentation", layout="wide")

# --- Taille des textes et Marges ---
st.markdown("""
<style>
    /* Réduire l'espace en haut de la page */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    html, body, p, li, .stMarkdown {
        font-size: 24px !important;
    }
    h1 { font-size: 60px !important; }
    h2 { font-size: 45px !important; }
    h3 { font-size: 35px !important; }
    .stAlert { font-size: 24px !important; }
    .stImageCaption { font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

# Contrôle des flèches pour passer les diapos
def navigation_clavier():
    components.html("""
    <script>
    const doc = window.parent.document;
    doc.addEventListener('keydown', function(e) {
        // Si Flèche Droite -> On cherche le bouton "Next"
        if (e.key === 'ArrowRight') {
            const buttons = doc.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.includes('Next ➡️')) {
                    btn.click();
                }
            });
        }
        // Si Flèche Gauche -> On cherche le bouton "Prev"
        if (e.key === 'ArrowLeft') {
            const buttons = doc.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.includes('⬅️ Prev')) {
                    btn.click();
                }
            });
        }
    });
    </script>
    """, height=0, width=0)

# Dictionnaire regroupant les pages
pages_dict = {
    "Diapo 1": diapo1,
    "Diapo 2": diapo2,
    "Diapo 3": diapo3,
    "Diapo 4": diapo4,
    "Diapo 5": diapo5,
    "Diapo 6": diapo6,
    "Diapo 7": diapo7,
    "Diapo 8": diapo8,
    "Diapo 9": diapo9,
    "Diapo 10": diapo10,
    "Diapo 11": diapo11,
    "Diapo 12": diapo12,
    "Diapo 13": diapo13,
    "Diapo 14": diapo14,
    "Diapo 15": diapo15,
    "Diapo 16": diapo16,
    "Diapo 17": diapo17,
    "Diapo 18": diapo18,
    "Diapo 19": diapo19,
    "Diapo 20": diapo20,
    "Diapo 21": diapo21,
    "Diapo 22": diapo22
}

pages = list(pages_dict.keys())

# --- MENU LATÉRAL & NAVIGATION ---
st.sidebar.title("summary")

# On initialise la page actuelle dans la mémoire si elle n'existe pas
if "page_actuelle" not in st.session_state:
    st.session_state.page_actuelle = pages[0]

# Fonction pour changer de page
def changer_page(delta):
    index_actuel = pages.index(st.session_state.page_actuelle)
    nouveau_index = (index_actuel + delta) % len(pages)
    st.session_state.page_actuelle = pages[nouveau_index]

col_prev, col_next = st.sidebar.columns(2)

if col_prev.button("⬅️ Prev"):
    changer_page(-1)
    st.rerun()

if col_next.button("Next ➡️"):
    changer_page(1)
    st.rerun()

selection = st.sidebar.radio(
    "Go to :", 
    pages, 
    key="page_actuelle"
)

# Appel de la fonction "show_page()" du fichier choisi
pages_dict[selection].show_page()

# Activation du contrôle au clavier
navigation_clavier()
