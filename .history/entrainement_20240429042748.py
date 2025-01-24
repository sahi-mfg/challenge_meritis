temps = []

with open("data2.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        temps.append(int(line))

print(temps[0:10])

longest_progression = []
for i in range(0, len(temps)):
    for j in range(i, len(temps)):
        progression = temps[j] - temps[i]
        if progression > 0:
            longest_progression.append(progression)

print(longest_progression[0:10])
