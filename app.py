import streamlit as st

from src.features.load_data import load_data
from src.pages.dataset import display_dataset
from src.pages.analyse import display_analysis_page
from src.pages.meilleurs_profils import display_best_profiles


st.set_page_config(
    page_title="Analyse des joueurs FIFA",
    layout="wide"
)


# Chargement des données
df = load_data("data/all_players_clean.csv")


# Navigation entre les pages
pages = {
    "Dataset": lambda: display_dataset(df),
    "Analyse": lambda: display_analysis_page(df),
    "Meilleurs profils": lambda: display_best_profiles(df)
}


st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "",
    pages.keys()
)


# Affichage de la page sélectionnée
pages[page]()