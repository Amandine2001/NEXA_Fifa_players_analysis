import streamlit as st

from src.analyses.joueurs import (
    display_best_players,
    display_top_players_by_stat
)

from src.analyses.graphes.radar import display_player_radar

from src.features.filtres import get_gender_filter, apply_gender_filter


def display_best_profiles(df):

    st.title("Analyse des joueurs FIFA - Meilleurs profils")
    
    st.write(
        "Identifiez les meilleurs joueurs selon leur note globale "
        "ou selon une qualité spécifique."
    )

    st.divider()

    gender = get_gender_filter(df)

    df_filtered = apply_gender_filter(df, gender)

    # Top 10 global selon OVR
    display_best_players(df_filtered)

    st.divider()

    # Top 10 selon une qualité
    display_top_players_by_stat(df_filtered)

    st.divider()

    # Comparaison de deux joueurs
    display_player_radar(df_filtered)