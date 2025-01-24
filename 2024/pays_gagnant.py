from collections import namedtuple
import pandas as pd  # type: ignore
import logging

logging.basicConfig(level=logging.DEBUG)

Item = namedtuple("Item", ["numero_dossard", "pays", "temps_en_ms"])

logging.info(f"Named tuple created: {Item.__name__}:{Item._fields}")

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

df_clean = df.groupby("pays")["temps_en_ms"].mean().reset_index()
df_clean = df_clean.sort_values(by="temps_en_ms", ascending=True)

# print(df_clean)


def get_pays_gagnant(df: pd.DataFrame) -> str:
    """
    Retourne le pays gagnant de la course
    """
    return df.loc[df["temps_en_ms"].idxmin()]["pays"]


if __name__ == "__main__":
    pays_gagnant = get_pays_gagnant(df_clean)
    print(f"Le pays gagnant est: {pays_gagnant}")
