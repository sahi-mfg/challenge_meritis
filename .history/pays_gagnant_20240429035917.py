from collections import namedtuple
import pandas as pd  # type: ignore

Item = namedtuple("Item", ["numero_dossard", "pays", "temps_en_ms"])
items = []

with open("data.txt", "r") as file:
    for line in file:
        numero_dossard = line.split(",")[0].rstrip("\n")
        pays = line.split(",")[1].rstrip("\n")
        temps_en_ms = line.split(",")[2].rstrip("\n")
        items.append(Item(numero_dossard, pays, temps_en_ms))

df = pd.DataFrame.from_records(items, columns=["numero_dossard", "pays", "temps_en_ms"])
df["temps_en_ms"] = df["temps_en_ms"].astype(int)
df["numero_dossard"] = df["numero_dossard"].astype(int)

# print(df.head())


def get_pays_gagnant(df: pd.DataFrame) -> str:
    """
    Retourne le pays gagnant de la course
    """
    return df.loc[df["temps_en_ms"].idxmin()]["pays"]


print(get_pays_gagnant(df))

print(df["temps_en_ms"].describe())
