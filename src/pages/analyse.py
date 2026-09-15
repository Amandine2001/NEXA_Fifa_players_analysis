import streamlit as st

from src.features.filtres import get_filters, apply_filters
from src.features.kpis import display_kpis

from src.analyses.graphes.distribution import display_distribution
from src.analyses.graphes.comparaison import display_measure_by_position
from src.analyses.graphes.relation import display_relationship
from src.analyses.graphes.heatmap import display_correlation_heatmap


def display_analysis_page(df):
    st.title("Analyse des joueurs FIFA - Analyse globale")

    st.write(
        "Utilisez les filtres pour sélectionner les joueurs "
        "et analyser leurs caractéristiques."
    )

    gender, league, position, nation, ovr_min, pac_min = get_filters(df)

    df_filtered = apply_filters(df, gender, league, position, nation, ovr_min, pac_min)

    if df_filtered.empty:
        st.warning("Aucun joueur ne correspond aux filtres sélectionnés.")
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
        "PHY",
    ]

    top_players = df_filtered[columns].sort_values("OVR", ascending=False).head(10)

    st.dataframe(top_players, use_container_width=True, hide_index=True)

    st.divider()

    # Graphiques
    """ col1, col2 = st.columns(2)

    with col1:
        display_ovr_distribution(df_filtered)

    with col2:
        display_ovr_by_position(df_filtered) """

    measure = st.selectbox(
        "Mesure à analyser", ["OVR", "PAC", "SHO", "PAS", "DRI", "DEF", "PHY"]
    )

    col1, col2 = st.columns(2)

    with col1:
        display_distribution(df_filtered, measure)

    with col2:
        display_measure_by_position(df_filtered, measure)

    st.divider()
    st.subheader("Relations entre les caractéristiques")

    variables = ["Age", "PAC", "SHO", "PAS", "DRI", "DEF", "PHY", "OVR"]

    col1, col2 = st.columns(2)

    with col1:
        x_variable = st.selectbox("Variable X", variables, index=0)

    with col2:
        y_variable = st.selectbox("Variable Y", variables, index=7)

    if x_variable == y_variable:
        st.warning("Veuillez sélectionner deux variables différentes.")
    else:
        display_relationship(df_filtered, x_variable, y_variable)

    """ display_relationship(
        df_filtered,
        x_variable,
        y_variable
    ) """

    st.divider()

    display_correlation_heatmap(df_filtered)
