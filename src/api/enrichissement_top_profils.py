import pandas as pd

def top10_masculin_et_top10_feminin(df):

    top10_male = (
        df[df["gender"] == "M"]
        .sort_values("OVR", ascending=False)
        .head(10)
    )

    top10_female = (
        df[df["gender"] == "F"]
        .sort_values("OVR", ascending=False)
        .head(10)
    )

    top20 = pd.concat([
        top10_male,
        top10_female
    ])

    return top20

if __name__ == '__main__':
    top20 = top10_masculin_et_top10_feminin(df=pd.read_csv(filepath_or_buffer='data/all_players_clean.csv'))
    print(top20.head(5))