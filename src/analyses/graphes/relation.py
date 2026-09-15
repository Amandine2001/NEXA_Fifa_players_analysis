import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def display_pas_dri_relationship(df):
    st.subheader("Relation entre PAS et DRI")

    st.caption(
        "Ce nuage de points permet d'étudier la relation entre les qualités de passe et de dribble des joueurs."
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(data=df, x="PAS", y="DRI", ax=ax)

    ax.set_xlabel("PAS")
    ax.set_ylabel("DRI")

    st.pyplot(fig)


def display_age_ovr_relationship(df):
    st.subheader("Âge et performance")
    st.caption("Relation entre l'âge des joueurs et leur note globale (OVR).")

    fig, ax = plt.subplots(figsize=(6, 3))

    sns.scatterplot(data=df, x="Age", y="OVR", ax=ax)

    sns.regplot(data=df, x="Age", y="OVR", scatter=False, ax=ax)

    ax.set_xlabel("Âge")
    ax.set_ylabel("OVR")

    st.pyplot(fig)
