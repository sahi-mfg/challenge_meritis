from collections import namedtuple
import pandas as pd  # type: ignore

Item = namedtuple("Item", ["id_athlete", "timestamp_in", "timestamp_out"])
items = []

with open("data3.txt", "r") as file:
    for line in file:
        id_athlete = line.split(",")[0].rstrip("\n")
        timestamp_in = line.split(",")[1].rstrip("\n")
        timestamp_out = line.split(",")[2].rstrip("\n")
        items.append(Item(id_athlete, timestamp_in, timestamp_out))

df = pd.DataFrame.from_records(
    items, columns=["id_athlete", "timestamp_in", "timestamp_out"]
)
# print(df.info())
df["timestamp_in"] = df["timestamp_in"].astype(int)
df["timestamp_out"] = df["timestamp_out"].astype(int)
df["id_athlete"] = df["id_athlete"].astype(int)


print(df["id_athlete"].nunique())
print(df["id_athlete"].value_counts())
