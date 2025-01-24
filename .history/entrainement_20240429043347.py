from typing import List

temps = []

with open("data2.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        temps.append(int(line))

# print(temps[0:10])

longest_sequence_progression: List[int] = []
for i in range(len(temps)):
    sequence_progression = [temps[i]]
    for j in range(i + 1, len(temps)):
        if temps[j] > sequence_progression[-1]:
            sequence_progression.append(temps[j])
    if len(sequence_progression) > len(longest_sequence_progression):
        longest_sequence_progression = sequence_progression
