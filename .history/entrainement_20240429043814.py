from typing import List

temps = []

with open("data2.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        temps.append(int(line))

# print(temps[0:10])


def longest_decreasing_sequence(temps: List[int]) -> List[int]:
    n = len(temps)
    dp = [1] * n
    prev_index = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if temps[i] < temps[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the longest increasing subsequence
    sequence = []
    while max_index != -1:
        sequence.append(temps[max_index])
        max_index = prev_index[max_index]

    sequence.reverse()

    return sequence


longest_sequence_progression = longest_decreasing_sequence(temps)
print(longest_sequence_progression)
