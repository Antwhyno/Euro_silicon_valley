import streamlit as st
import time

# --- CONFIGURATION DE LA PAGE (Moderne & Large) ---
st.set_page_config(
    page_title="Concorde: La Légende Supersonique",
    page_icon="✈️",
    layout="wide",  # Utilise toute la largeur de l'écran
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONNALISÉ (Pour quelques touches modernes supplémentaires) ---
# Streamlit est limité en CSS natif, mais on peut injecter un peu de style
# pour améliorer les titres et l'espacement.
st.markdown("""
    <style>
    .main-header {
        font-size: 3em !important;
        color: #1E3A8A; /* Bleu nuit moderne */
        text-align: center;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.5em !important;
        text-align: center;
        color: #4B5563;
        margin-bottom: 30px;
    }
    /* Amélioration visuelle des métriques */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        color: #004e92;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECTION HÉROS (Image d'intro) ---
# Note: J'utilise des images Wikimedia publiques. Pour un vrai projet,
# tu devrais télécharger ces images et les mettre dans ton dossier local.
hero_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Concorde_on_Bristol_Filton_airfield_%28crop%29.jpg/1920px-Concorde_on_Bristol_Filton_airfield_%28crop%29.jpg"

st.image(hero_image, use_column_width=True)
st.markdown('<p class="main-header">LE CONCORDE</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">L\'ingénierie à la frontière du son</p>', unsafe_allow_html=True)
st.markdown("---")

# --- SECTION 1 : LES STATS CLÉS (Tableau de bord moderne) ---
st.header("⚡ Plus vite que le Soleil")
st.write("Il volait si vite qu'en allant vers l'ouest, vous arriviez avant d'être parti (heure locale).")

# Utilisation de 4 colonnes pour un affichage "dashboard"
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Vitesse Max", value="Mach 2.04", delta="2 179 km/h")
with col2:
    st.metric(label="Altitude de croisière", value="60 000 ft", delta="≈ 18 km d'altitude")
with col3:
    st.metric(label="Passagers", value="92 - 128", delta="Service exclusif")
with col4:
    # Exemple de petit calcul dynamique
    ny_london_time = "≈ 3h 30min"
    st.metric(label="Paris/Londres -> NYC", value=ny_london_time, delta="-4h vs vol normal", delta_color="inverse")

st.markdown("---")

# --- SECTION 2 : L'EXPÉRIENCE (Interactive) ---
st.header("🕰️ La différence supersonique")

# Création de deux colonnes : une pour le texte/contrôle, une pour le résultat visuel
col_interact_text, col_interact_viz = st.columns([1, 2])

with col_interact_text:
    st.write("Comparez un vol long-courrier classique avec l'expérience Concorde.")
    # Un slider pour rendre la page interactive
    standard_flight = st.slider("Durée d'un vol subsonique classique (heures) :", min_value=6, max_value=14, value=8)
    
    # Calcul approximatif : Concorde allait environ 2.2x plus vite
    concorde_duration = standard_flight / 2.2

    if st.button("Calculer le temps Concorde 🚀"):
        with st.spinner("Passage du mur du son..."):
            time.sleep(0.8) # Petite pause pour l'effet dramatique
        
        st.balloons() # Effet visuel Streamlit
        st.success(f"Temps de vol Concorde estimé : **{concorde_duration:.1f} heures**.")

with col_interact_viz:
    # Utilisation de barres de progression pour visualiser la différence
    st.write(f"**Vol Classique ({standard_flight}h)**")
    st.progress(100) # 100% du temps
    
    st.write(f"**Vol Concorde (≈{concorde_duration:.1f}h)**")
    # Calcul du pourcentage pour la barre de progression
    progress_value = int((concorde_duration / standard_flight) * 100)
    st.progress(progress_value)
    st.caption("Le Concorde transformait un voyage fatigant en un simple déjeuner d'affaires.")


st.markdown("---")

# --- SECTION 3 : DESIGN ET INGÉNIERIE (Layout mixte) ---
st.header("🎨 Une icône du design industriel")

col_design_img, col_design_text = st.columns([1, 2])

with col_design_img:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Concorde_at_Filton.jpg", caption="Le célèbre 'nez basculant' (Droop Nose) en position basse.")

with col_design_text:
    st.subheader("L'aile Delta Ogivale")
    st.write("""
    Fruit d'une collaboration franco-britannique (Aérospatiale et BAC), le Concorde est immédiatement reconnaissable à son aile "delta ogivale". 
    Cette forme complexe était le compromis parfait : suffisamment de portance à basse vitesse pour décoller, et une traînée minimale à Mach 2.
    """)
    
    # Utilisation d'un "expander" pour cacher les détails techniques et garder la page épurée
    with st.expander("Pourquoi le nez bougeait-il ? (Le Droop Nose)"):
        st.write("""
        À cause de son aile delta, le Concorde devait atterrir avec un angle très cabré (le nez très haut). 
        Les pilotes ne pouvaient donc pas voir la piste !
        La solution ? Un nez hydraulique qui s'abaissait de 12,5 degrés pour le décollage et l'atterrissage, offrant une visibilité parfaite, avant de se relever pour le vol supersonique.
        """)

st.markdown("---")

# --- PIED DE PAGE ---
st.subheader("🌅 La fin d'une ère")
st.write("Retiré du service en 2003, victime de ses coûts d'exploitation, du 'bang' supersonique qui limitait ses routes au-dessus des océans, et du tragique crash de Gonesse en 2000. Il reste à ce jour le seul avion de ligne supersonique à avoir connu un succès commercial durable.")

st.caption("Développé avec Python & Streamlit. Images : Wikimedia Commons.")