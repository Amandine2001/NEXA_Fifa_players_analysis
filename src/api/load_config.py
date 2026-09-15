import configparser
import streamlit as st


def load_config():

    # Sur Streamlit Cloud
    if "PLAYER_ELO_API_KEY" in st.secrets:
        return {
            "BASE_URL": config["DEFAULT"]["BASE_URL"],
            "PLAYER_ELO_API_KEY": config["DEFAULT"]["PLAYER_ELO_API_KEY"],
        }

    # En local
    config = configparser.ConfigParser()
    config.read("config.properties")

    return {
        "BASE_URL": config["DEFAULT"]["BASE_URL"],
        "PLAYER_ELO_API_KEY": config["DEFAULT"]["PLAYER_ELO_API_KEY"],
    }
