from collections import namedtuple

Item = namedtuple("Item", ["numero_dossard", "pays", "temps(en ms)"])
items = []

with open("data.txt", "r") as file:
    for line in file:
        l = line.rstrip("\n").split(",")
        print(l)
