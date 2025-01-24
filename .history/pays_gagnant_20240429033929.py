from collections import namedtuple

Item = namedtuple("Item", ["numero_dossard", "pays", "temps_en_ms"])
items = []

with open("data.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n").split(",")
        print(line)
