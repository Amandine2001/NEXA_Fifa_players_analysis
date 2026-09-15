import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy.stats import linregress


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


def display_relationship(df, x_variable, y_variable):
    st.subheader(f"{y_variable} selon {x_variable}")

    st.caption(
        f"Ce graphique permet d'étudier la relation entre {x_variable} et {y_variable}."
    )

    if x_variable == y_variable:
        st.warning("Veuillez sélectionner deux variables différentes.")
        return

    data = df[[x_variable, y_variable]].dropna()

    if data.empty:
        st.warning("Impossible d'afficher la relation : aucune donnée disponible.")
        return

    if data[x_variable].nunique() < 2:
        st.warning(
            f"Impossible de calculer la régression : "
            f"{x_variable} ne contient pas suffisamment de valeurs différentes."
        )
        return

    regression = linregress(data[x_variable], data[y_variable])

    slope = regression.slope
    intercept = regression.intercept
    r_squared = regression.rvalue**2

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(data=data, x=x_variable, y=y_variable, ax=ax)

    sns.regplot(
        data=data,
        x=x_variable,
        y=y_variable,
        scatter=False,
        ax=ax,
        line_kws={"color": "red"},
    )

    ax.set_xlabel(x_variable)
    ax.set_ylabel(y_variable)

    equation = rf"$y = {slope:.2f}x + {intercept:.2f}$"

    ax.text(
        0.05,
        0.95,
        f"{equation}\n$R^2 = {r_squared:.2f}$",
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment="top",
        bbox=dict(
            boxstyle="round,pad=0.5", facecolor="white", edgecolor="black", alpha=0.9
        ),
    )

    st.pyplot(fig)
