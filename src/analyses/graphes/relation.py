import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def display_pas_dri_relationship(df):
    st.subheader("Relation entre PAS et DRI")

    st.caption(
        "Ce nuage de points permet d'étudier la relation entre les qualités de passe et de dribble des joueurs."
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=df,
        x="PAS",
        y="DRI",
        ax=ax
    )

    ax.set_xlabel("PAS")
    ax.set_ylabel("DRI")

    st.pyplot(fig)