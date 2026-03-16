import streamlit as st

# --- CONFIGURATION DE LA PRÉSENTATION ---
st.set_page_config(
    page_title="The Concorde Presentation",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS POUR LE MODE "TABLEAU DE CLASSE" (Texte Gros) ---
st.markdown("""
    <style>
    /* Grossir tout le texte de base */
    .stMarkdown p, .stMarkdown li {
        font-size: 24px !important;
        line-height: 1.6 !important;
    }
    /* Grossir les titres */
    h1 { font-size: 60px !important; text-align: center; color: #1E3A8A; }
    h2 { font-size: 45px !important; color: #DC2626; border-bottom: 2px solid #ccc; }
    h3 { font-size: 35px !important; color: #1F2937; }
    
    /* Cacher les éléments parasites de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Style des encadrés d'info */
    .stAlert { font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION (SOMMAIRE) ---
# On utilise la barre latérale comme télécommande pour changer de diapo
slides = [
    "1. Intro & Context",
    "2. The Partnership",
    "3. The Supersonic Race",
    "4. Aerodynamics (Wings)",
    "5. Engines & Speed",
    "6. Cockpit Innovations",
    "7. Life on Board",
    "8. The End of the Dream",
    "9. Conclusion & Legacy"
]

st.sidebar.title("Navigation")
current_slide = st.sidebar.radio("Go to slide:", slides)
st.sidebar.markdown("---")
st.sidebar.info("Tip: Appuie sur **F11** pour mettre ton navigateur en plein écran !")

# --- CONTENU DES DIAPOSITIVES ---

# === SLIDE 1 : INTRODUCTION & CONTEXTE ===
if current_slide == "1. Intro & Context":
    st.title("THE CONCORDE: A Legend")
    st.subheader("Context: The late 1950s & The Cold War")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        * **Date:** Late 1950s - Early 1960s.
        * **Context:** The **Cold War**. A race for technological superiority.
        * **The Goal:** Show power through science and speed.
        * **The Dream:** Cross the Atlantic in less than 4 hours.
        """)
        st.info("At this time, planes used propellers or early jets. Speed was the new frontier.")

    with col2:
        # Image d'époque symbolisant les années 60/Aviation
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Concorde_on_Bristol_Filton_airfield_%28crop%29.jpg", caption="The Concorde: Symbol of a new era.")

# === SLIDE 2 : PARTENARIAT ===
elif current_slide == "2. The Partnership":
    st.title("🇫🇷 A Historic Collaboration 🇬🇧")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Concorde_101_G-AXDN_filton.jpg", caption="British and French engineering combined.")
    
    with col2:
        st.markdown("""
        * **The Treaty:** Signed on **November 29, 1962**.
        * **Countries:** France & Great Britain.
        * **Companies:** * **Sud-Aviation** (became Aérospatiale) - *France*
            * **British Aircraft Corporation (BAC)** - *UK*
        """)
        st.warning("They joined forces to share the colossal costs and knowledge.")

# === SLIDE 3 : LA COURSE SUPERSONIQUE ===
elif current_slide == "3. The Supersonic Race":
    st.title("The Supersonic Race")
    st.write("Europe was not alone. The whole world wanted to fly supersonic.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("1. The Concorde")
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Air_France_Concorde.jpg")
        st.write("🇪🇺 **Europe**")
        st.write("Technologically successful.")

    with col2:
        st.subheader("2. Tupolev Tu-144")
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Tupolev_Tu-144_on_the_MAKS-2011_%2803%29.jpg")
        st.write("🇷🇺 **USSR**")
        st.write("Nicknamed 'Concordski'. Faster but louder and unsafe.")

    with col3:
        st.subheader("3. Boeing 2707")
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Boeing_2707_mockup.jpg")
        st.write("🇺🇸 **USA**")
        st.write("Project cancelled in 1971 (Too expensive).")

# === SLIDE 4 : CARACTÉRISTIQUES (AILES) ===
elif current_slide == "4. Aerodynamics (Wings)":
    st.title("Technological Marvel: The Wings")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        * **Shape:** "Gothic Delta Wings" (Ogival).
        * **Why?** 1.  Extremely aerodynamic at **Mach 2**.
            2.  Creates "Vortex Lift" at low speed (landing).
        * **Specific:** No flaps or slats! The shape does everything.
        """)
    
    with col2:
        # Schéma ou photo des ailes
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Concorde_at_Filton.jpg", caption="The Gothic Delta Wing shape.")

# === SLIDE 5 : MOTEURS ===
elif current_slide == "5. Engines & Speed":
    st.title("Power: Rolls-Royce / SNECMA")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/93/Concorde_Olympus_593_afterburner.jpg", caption="Olympus 593 Turbojet with Afterburner.")
    
    with col2:
        st.markdown("""
        * **Engines:** 4x Olympus 593 turbojets.
        * **Reheat (Afterburner):** Just like a fighter jet! Used for takeoff and breaking the sound barrier.
        * **The System:** Movable intake ramps slowed the air down before entering the engine.
        """)
        st.success("**Max Speed:** Mach 2.04 (≈ 2,179 km/h)\n\n**Altitude:** 60,000 ft (Standard planes fly at 35,000 ft).")

# === SLIDE 6 : INNOVATIONS COCKPIT ===
elif current_slide == "6. Cockpit Innovations":
    st.title("Decades Ahead of Time")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("The Droop Nose")
        st.markdown("""
        * **Problem:** Pilots couldn't see the runway during landing due to the steep angle.
        * **Solution:** The nose tilted down by **12.5 degrees**.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/a2/Concorde_Final_Flight_%28crop%29.jpg", caption="Nose down for landing.")

    with col2:
        st.subheader("Fly-By-Wire")
        st.markdown("""
        * **Revolution:** First airliner to use **electric flight orders** instead of mechanical cables.
        * **Ancestor of FADEC:** Digital engine control.
        * **Autopilot:** Could manage the plane entirely at Mach 2.
        """)

# === SLIDE 7 : LA VIE A BORD ===
elif current_slide == "7. Life on Board":
    st.title("Flying Faster than the Sun")
    
    st.markdown("""
    > "It turned a 12-hour journey into a short afternoon trip."
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Passengers", value="100", delta="Exclusive Service")
        st.metric(label="Paris -> NYC", value="3h 30min", delta="-4h vs Boeing 747")
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/Concorde_interior.jpg", caption="A narrow but luxury cabin.")

# === SLIDE 8 : LA FIN ===
elif current_slide == "8. The End of the Dream":
    st.title("Why did it stop?")
    st.error("Retirement: 2003")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **1. The Crash (Gonesse, 2000):**
        * Flight 4590. A tire burst caused a fire.
        * 113 fatalities. Broken trust.
        
        **2. Economics:**
        * Ticket price was too high (€8,000+).
        * Huge fuel consumption.
        * Post-9/11 aviation crisis.
        """)
    
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/ee/Concorde_on_barge.jpg", caption="The Concorde became a museum piece.")

# === SLIDE 9 : CONCLUSION ===
elif current_slide == "9. Conclusion & Legacy":
    st.title("Conclusion: A Lasting Legacy")
    
    st.markdown("Even if Concorde stopped, it changed everything.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Airbus")
        st.write("The cooperation proved Europe could build planes together.")
    
    with col2:
        st.subheader("Technology")
        st.write("Fly-by-wire & FADEC are now standard on all planes.")
        
    with col3:
        st.subheader("The Future")
        st.write("NASA X-59: Trying to make supersonic flight *silent*.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/ce/Low_Speed_Chase_Plane_Video_of_X-59_QueSST_%28NASA_Video%29.jpg", caption="NASA X-59")

    st.markdown("---")
    st.success("Thank you for listening! Would you have liked to fly on Concorde?")