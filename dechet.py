def find_most_frequent(data: list[int]) -> dict[int, int]:
    frequency: dict[int, int] = {}
    for i in data:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        raw_data = f.read()

    data: list[int] = list(map(int, raw_data.split()))
    result = find_most_frequent(data)
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    print(sorted_result)
