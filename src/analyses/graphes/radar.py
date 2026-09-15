import streamlit as st
import pandas as pd
import plotly.express as px


def display_player_radar(df):

    st.subheader("Comparer deux joueurs")

    stats = ["PAC", "SHO", "PAS", "DRI", "DEF", "PHY"]

    joueurs = sorted(df["Name"].dropna().unique())

    col1, col2 = st.columns(2)

    with col1:
        joueur1 = st.selectbox("Premier joueur", joueurs, key="joueur1")

    with col2:
        joueur2 = st.selectbox(
            "Deuxième joueur",
            joueurs,
            index=1 if len(joueurs) > 1 else 0,
            key="joueur2",
        )

    df_comparaison = df[df["Name"].isin([joueur1, joueur2])]

    radar_df = df_comparaison[["Name"] + stats].melt(
        id_vars="Name", var_name="stat", value_name="valeur"
    )

    fig = px.line_polar(
        radar_df,
        r="valeur",
        theta="stat",
        color="Name",
        line_close=True,
        title="Comparaison des profils",
    )

    fig.update_layout(polar=dict(radialaxis=dict(range=[0, 100])))

    st.plotly_chart(fig, use_container_width=True)
