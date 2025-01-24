import os

print(os.getcwd())


def find_most_frequent(data: list[int]) -> dict[int, int]:
    frequency: dict[int, int] = {}
    for i in data:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    file_path = os.path.join(script_dir, "../data/2025/data.txt")
    with open(file_path, "r") as f:
        raw_data = f.read()

    data: list[int] = list(map(int, raw_data.split()))
    result = find_most_frequent(data)
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    print(sorted_result)
