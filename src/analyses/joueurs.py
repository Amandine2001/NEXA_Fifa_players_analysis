import streamlit as st


def display_best_players(df):
    st.subheader("Meilleurs profils selon les performances (OVR)")

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
        df[columns]
        .sort_values("OVR", ascending=False)
        .head(10)
    )

    st.dataframe(
        top_players,
        use_container_width=True,
        hide_index=True
    )

def display_top_players_by_stat(df):
    st.subheader("Top 10 par qualité")

    stats = [
        "PAC",
        "SHO",
        "PAS",
        "DRI",
        "DEF",
        "PHY"
    ]

    stat = st.selectbox(
        "Choisissez une qualité",
        stats
    )

    columns = [
        "Name",
        "League",
        "Nation",
        "Position",
        stat
    ]

    top_players = (
        df[columns]
        .sort_values(stat, ascending=False)
        .head(10)
    )

    st.dataframe(
        top_players,
        use_container_width=True,
        hide_index=True
    )