import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def display_ovr_by_position(df):
    st.subheader("OVR selon le poste")

    st.caption(
        "Ce boxplot permet de comparer le niveau et la dispersion des OVR entre les différents postes."
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.boxplot(
        data=df,
        x="Position",
        y="OVR",
        ax=ax
    )

    ax.set_xlabel("Poste")
    ax.set_ylabel("OVR")

    st.pyplot(fig)