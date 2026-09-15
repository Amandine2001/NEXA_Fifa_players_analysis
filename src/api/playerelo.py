import os
import pandas as pd
import requests

from enrichissement_top_profils import top10_masculin_et_top10_feminin
from load_config import load_config


def search_player(name):
    config = load_config()

    url = f"{config['BASE_URL']}/v1/players"

    headers = {"Authorization": f"Bearer {config['PLAYER_ELO_API_KEY']}"}

    params = {"search": name, "limit": 1}

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    return response.json()


def get_player_id(name):
    result = search_player(name)

    if not result:
        return None

    return result[0]["player_id"]


def get_market_value(player_id):
    config = load_config()

    url = f"{config['BASE_URL']}/v1/players/{player_id}/value"

    headers = {"Authorization": f"Bearer {config['PLAYER_ELO_API_KEY']}"}

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    data = response.json()

    return data["estimated_value"]


def get_player_info(name):
    result = search_player(name)

    if not result:
        return None, None

    player_id = result[0]["player_id"]
    market_value = get_market_value(player_id)

    return player_id, market_value


def add_playerelo_data(df):
    df = df.copy()

    player_ids = []
    market_values = []

    for name in df["Name"]:
        player_id, market_value = get_player_info(name)

        player_ids.append(player_id)
        market_values.append(market_value)

    df["player_id"] = player_ids
    df["valeur_marchande"] = market_values

    return df


if __name__ == "__main__":
    """ result = search_player("Kylian Mbappé")
    print(result)

    player_id = get_player_id("Kylian Mbappé")
    print(player_id)

    value = get_market_value(player_id)
    print("Valeur marchande :", value)

    player_id, market_value = get_player_info("Kylian Mbappé")
    print(player_id)
    print(market_value) """

    top20 = top10_masculin_et_top10_feminin(
        df=pd.read_csv(filepath_or_buffer="data/all_players_clean.csv")
    )
    top20 = add_playerelo_data(top20)

    top20.to_csv("data/top_players_values.csv", index=False)
