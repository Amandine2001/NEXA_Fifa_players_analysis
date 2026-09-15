import streamlit as st

def get_filters(df):
    st.sidebar.header("Filtres")

    gender = st.sidebar.selectbox(
        "Genre",
        ["Tous"] + sorted(df["gender"].dropna().unique())
    )

    league = st.sidebar.selectbox(
        "Championnat",
        ["Tous"] + sorted(df["League"].dropna().unique())
    )

    position = st.sidebar.selectbox(
        "Poste",
        ["Tous"] + sorted(df["Position"].dropna().unique())
    )

    nation = st.sidebar.selectbox(
        "Nationalité",
        ["Toutes"] + sorted(df["Nation"].dropna().unique())
    )

    ovr_min = st.sidebar.slider(
        "OVR minimum",
        min_value=int(df["OVR"].min()),
        max_value=int(df["OVR"].max()),
        value=int(df["OVR"].min())
    )

    pac_min = st.sidebar.slider(
        "PAC minimum",
        min_value=int(df["PAC"].min()),
        max_value=int(df["PAC"].max()),
        value=int(df["PAC"].min())
    )

    return gender, league, position, nation, ovr_min, pac_min


def apply_filters(df, gender, league, position, nation, ovr_min, pac_min):
    df_filtered = df.copy()

    if gender != "Tous":
        df_filtered = df_filtered[df_filtered["gender"] == gender]

    if league != "Tous":
        df_filtered = df_filtered[df_filtered["League"] == league]

    if position != "Tous":
        df_filtered = df_filtered[df_filtered["Position"] == position]

    if nation != "Toutes":
            df_filtered = df_filtered[df_filtered["Nation"] == nation]

    df_filtered = df_filtered[df_filtered["OVR"] >= ovr_min]
    df_filtered = df_filtered[df_filtered["PAC"] >= pac_min]

    return df_filtered

def get_gender_filter(df):
    return st.sidebar.selectbox(
        "Genre",
        ["Tous"] + sorted(df["gender"].dropna().unique())
    )

def apply_gender_filter(df, gender):
    df_filtered = df.copy()

    if gender != "Tous":
        df_filtered = df_filtered[df_filtered["gender"] == gender]

    return df_filtered