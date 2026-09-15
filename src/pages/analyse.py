import streamlit as st

from src.features.filtres import get_filters, apply_filters
from src.features.kpis import display_kpis

from src.analyses.graphes.distribution import display_ovr_distribution
from src.analyses.graphes.comparaison import display_ovr_by_position
from src.analyses.graphes.relation import display_pas_dri_relationship
from src.analyses.graphes.heatmap import display_correlation_heatmap


def display_analysis_page(df):
    st.title("Analyse des joueurs FIFA - Analyse globale")

    st.write(
        "Utilisez les filtres pour sélectionner les joueurs "
        "et analyser leurs caractéristiques."
    )

    gender, league, position, nation, ovr_min, pac_min = get_filters(df)

    df_filtered = apply_filters(
        df,
        gender,
        league,
        position,
        nation,
        ovr_min,
        pac_min
    )

    if df_filtered.empty:
        st.warning(
            "Aucun joueur ne correspond aux filtres sélectionnés."
        )
        return
    
    st.divider()

    # KPIs
    display_kpis(df_filtered)

    st.divider()

    # Tableau des joueurs sélectionnés
    st.subheader("Top 10 des joueurs en fonction de la sélection")

    columns = [
        "Name",
        "League",
        "Nation",
        "Position",
        "OVR",
        "PAC",
        "SHO",
        "PAS",
        "DRI",
        "DEF",
        "PHY"
    ]

    top_players = (
        df_filtered[columns]
        .sort_values("OVR", ascending=False)
        .head(10)
    )

    st.dataframe(
        top_players,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Graphiques
    display_ovr_distribution(df_filtered)

    display_ovr_by_position(df_filtered)

    display_pas_dri_relationship(df_filtered)

    st.divider()

    display_correlation_heatmap(df_filtered)