temps = []

with open("data2.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        temps.append(int(line))

print(temps[0:5])
