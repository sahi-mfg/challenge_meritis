from collections import namedtuple

Item = namedtuple("Item", ["numero_dossard", "pays", "temps_en_ms"])
items = []

with open("data.txt", "r") as file:
    for line in file:
        numero_dossard = line.split(",")[0].rstrip("\n")
        pays = line.split(",")[1].rstrip("\n")
        temps_en_ms = line.split(",")[2].rstrip("\n")
        items.append(Item(numero_dossard, pays, temps_en_ms))
        print(items)
