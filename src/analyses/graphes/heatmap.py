import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def display_correlation_heatmap(df):
    st.subheader("Corrélation entre les statistiques")

    st.caption(
        "Cette heatmap permet d'identifier les statistiques les plus liées "
        "entre elles et avec la note globale OVR."
    )

    stats = [
        "PAC",
        "SHO",
        "PAS",
        "DRI",
        "DEF",
        "PHY",
        "OVR"
    ]

    correlation = df[stats].corr()

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax
    )

    ax.set_title("Matrice de corrélation des statistiques")

    st.pyplot(fig)