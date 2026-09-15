import streamlit as st


def display_dataset(df):
    st.title("Analyse des joueurs FIFA - Le dataset")

    st.write(
        "Explorez les caractéristiques de joueurs de football afin de comparer leurs performances et d'identifier les meilleurs profils."
    )

    st.write(
        "Le dataset contient des informations sur les joueurs, "
        "leur championnat, leur nation, leur poste ainsi que différentes "
        "statistiques de performance."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Joueurs", len(df), border=True)
    col2.metric("Championnats", df["League"].nunique(), border=True)
    col3.metric("Nations", df["Nation"].nunique(), border=True)
    col4.metric("Postes", df["Position"].nunique(), border=True)

    st.subheader("Aperçu des données")

    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Principales statistiques")

        stats = {
            "OVR — Note globale": "Évalue le niveau général du joueur.",
            "PAC — Vitesse": "Évalue la vitesse et l'accélération du joueur.",
            "SHO — Tir": "Évalue les capacités de tir du joueur.",
            "PAS — Passe": "Évalue les capacités de passe du joueur.",
            "DRI — Dribble": "Évalue les capacités techniques et de dribble.",
            "DEF — Défense": "Évalue les capacités défensives du joueur.",
            "PHY — Physique": "Évalue les caractéristiques physiques du joueur.",
        }

        for variable, description in stats.items():
            st.write(f"**{variable}** — {description}")

    with col2:
        st.subheader("Postes")

        positions = {
            "GK — Gardien de but": "Goalkeeper",
            "CB — Défenseur central": "Centre Back",
            "LB — Arrière gauche": "Left Back",
            "RB — Arrière droit": "Right Back",
            "LWB — Piston gauche": "Left Wing Back",
            "RWB — Piston droit": "Right Wing Back",
            "CDM — Milieu défensif": "Central Defensive Midfielder",
            "CM — Milieu central": "Central Midfielder",
            "CAM — Milieu offensif": "Central Attacking Midfielder",
            "LM — Milieu gauche": "Left Midfielder",
            "RM — Milieu droit": "Right Midfielder",
            "LW — Ailier gauche": "Left Winger",
            "RW — Ailier droit": "Right Winger",
            "ST — Attaquant": "Striker",
            "CF — Avant-centre": "Centre Forward",
        }

        for position, description in positions.items():
            st.write(f"**{position}** — {description}")
