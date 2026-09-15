import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def display_ovr_distribution(df):
    st.subheader("Distribution des OVR")

    st.caption(
        "Cet histogramme permet d'observer la répartition du niveau global des joueurs sélectionnés."
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="OVR",
        bins=15,
        ax=ax
    )

    ax.set_xlabel("OVR")
    ax.set_ylabel("Nombre de joueurs")

    st.pyplot(fig)