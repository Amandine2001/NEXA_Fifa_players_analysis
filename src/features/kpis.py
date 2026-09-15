import streamlit as st


def display_kpis(df):
    # Première ligne
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Joueurs sélectionnés", len(df), border=True)

    col2.metric("OVR moyen", round(df["OVR"].mean(), 1), border=True)

    col3.metric("PAC moyen", round(df["PAC"].mean(), 1), border=True)

    col4.metric("SHO moyen", round(df["SHO"].mean(), 1), border=True)

    # Deuxième ligne
    col5, col6, col7, col8 = st.columns(4)

    col5.metric("PAS moyen", round(df["PAS"].mean(), 1), border=True)

    col6.metric("DRI moyen", round(df["DRI"].mean(), 1), border=True)

    col7.metric("DEF moyen", round(df["DEF"].mean(), 1), border=True)

    col8.metric("PHY moyen", round(df["PHY"].mean(), 1), border=True)
