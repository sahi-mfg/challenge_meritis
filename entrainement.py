from typing import List
import bisect

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
        if temps[i] < dp[-1]:
            dp.append(temps[i])
            prev_index[i] = len(dp) - 2
        else:
            # Find the position to replace
            pos = bisect.bisect_right(dp, temps[i])
            dp[pos - 1] = temps[i]
            prev_index[i] = pos - 1 if pos > 0 else -1

    sequence = []
    max_index = len(dp) - 1
    while max_index != -1:
        sequence.append(dp[max_index])
        max_index = prev_index[temps.index(dp[max_index])]

    sequence.reverse()

    return sequence


longest_sequence_progression = longest_decreasing_sequence(temps)
print(longest_sequence_progression)
