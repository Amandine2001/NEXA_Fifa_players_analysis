import streamlit as st

from src.analyses.joueurs import display_best_players, display_top_players_by_stat

from src.analyses.graphes.radar import display_player_radar

from src.features.filtres import get_gender_filter, apply_gender_filter


""" def display_best_profiles(df):

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
    display_player_radar(df_filtered) """

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def display_best_profiles(df):
    st.title("Meilleurs profils")

    st.write(
        "Comparez les meilleurs joueurs selon leur genre et leurs "
        "caractéristiques de performance."
    )

    # ============================================================
    # 1. Comparaison hommes / femmes
    # ============================================================

    st.divider()
    st.subheader("Comparaison hommes / femmes")

    col1, col2 = st.columns(2)

    # ------------------------------------------------------------
    # Répartition hommes / femmes
    # ------------------------------------------------------------

    with col1:
        st.write("Répartition des joueurs")

        gender_counts = df["gender"].value_counts()

        labels = []
        values = []

        if "M" in gender_counts:
            labels.append("Hommes")
            values.append(gender_counts["M"])

        if "F" in gender_counts:
            labels.append("Femmes")
            values.append(gender_counts["F"])

        fig, ax = plt.subplots(figsize=(2, 2))

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 5},
        )

        st.pyplot(fig, use_container_width=False)

        plt.close(fig)

    # ------------------------------------------------------------
    # Top 3 hommes / femmes
    # ------------------------------------------------------------

    with col2:
        st.write("Top 3")

        measure = st.selectbox(
            "Critère de classement", ["OVR", "PAC", "SHO", "PAS", "DRI", "DEF", "PHY"]
        )

        top_men = df[df["gender"] == "M"].dropna(subset=[measure]).nlargest(3, measure)

        top_women = (
            df[df["gender"] == "F"].dropna(subset=[measure]).nlargest(3, measure)
        )

        col_men, col_women = st.columns(2)

        with col_men:
            st.caption("Hommes")

            if top_men.empty:
                st.info("Aucun joueur disponible.")
            else:
                for rank, (_, player) in enumerate(top_men.iterrows(), start=1):
                    st.write(f"**{rank}e — {player['Name']}**")
                    st.caption(f"{measure} : {player[measure]}")

        with col_women:
            st.caption("Femmes")

            if top_women.empty:
                st.info("Aucune joueuse disponible.")
            else:
                for rank, (_, player) in enumerate(top_women.iterrows(), start=1):
                    st.write(f"**{rank}e — {player['Name']}**")
                    st.caption(f"{measure} : {player[measure]}")

    # ============================================================
    # 2. Top 10 joueurs
    # ============================================================

    st.divider()
    st.subheader("Meilleurs joueurs")

    measure_top10 = st.selectbox(
        "Caractéristique",
        ["OVR", "PAC", "SHO", "PAS", "DRI", "DEF", "PHY"],
        key="top10_measure",
    )

    top_10 = (
        df[["Name", "gender", measure_top10]]
        .dropna()
        .nlargest(5, measure_top10)
        .sort_values(measure_top10)
    )

    if top_10.empty:
        st.warning("Aucun joueur disponible pour cette caractéristique.")
    else:
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            fig, ax = plt.subplots(figsize=(4, 3))

            ax.barh(top_10["Name"], top_10[measure_top10])

            ax.set_xlabel(measure_top10, fontsize=5)

            ax.set_ylabel("Joueur", fontsize=5)

            ax.tick_params(axis="both", labelsize=5)

            st.pyplot(fig, use_container_width=False)

            plt.close(fig)

    # ============================================================
    # 3. Comparaison de deux joueurs
    # ============================================================

    st.divider()
    st.subheader("Comparer deux joueurs")

    players = sorted(df["Name"].dropna().unique())

    if len(players) < 2:
        st.warning("Il faut au moins deux joueurs pour effectuer une comparaison.")
        return

    col1, col2 = st.columns(2)

    with col1:
        player_1 = st.selectbox("Joueur 1", players)

    with col2:
        player_2 = st.selectbox("Joueur 2", players, index=1)

    if player_1 == player_2:
        st.warning("Veuillez sélectionner deux joueurs différents.")
        return

    player_1_data = df[df["Name"] == player_1].iloc[0]

    player_2_data = df[df["Name"] == player_2].iloc[0]

    categories = ["PAC", "SHO", "PAS", "DRI", "DEF", "PHY"]

    values_1 = [player_1_data[category] for category in categories]

    values_2 = [player_2_data[category] for category in categories]

    values_1 += values_1[:1]
    values_2 += values_2[:1]

    categories_radar = categories + categories[:1]

    angles = np.linspace(0, 2 * np.pi, len(categories_radar))

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        fig, ax = plt.subplots(figsize=(3, 3), subplot_kw={"polar": True})

        ax.plot(angles, values_1, label=player_1)

        ax.fill(angles, values_1, alpha=0.15)

        ax.plot(angles, values_2, label=player_2)

        ax.fill(angles, values_2, alpha=0.15)

        ax.set_xticks(angles[:-1])

        ax.set_xticklabels(categories, fontsize=5)

        ax.set_ylim(0, 100)

        ax.tick_params(axis="y", labelsize=5)

        ax.legend(fontsize=5, loc="upper right", bbox_to_anchor=(1.25, 1.1))

        st.pyplot(fig, use_container_width=False)

        plt.close(fig)
