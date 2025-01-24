from collections import namedtuple

Item = namedtuple("Item", ["numero_dossard", "pays", "temps_en_ms"])
items = []

with open("data.txt", "r") as file:
    for line in file:
        numero_dossard = line.split(",")[0]
        pays = line.split(",")[1]
        temps_en_ms = line.split(",")[2]
        items.append(Item(numero_dossard, pays, temps_en_ms))
        print(items)
