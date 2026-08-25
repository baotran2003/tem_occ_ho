if __name__ == "__main__":
    arr: list[int] = [1, 5, 3, 0, 8, 8, 9, 9]

    frequency_map: dict[int, int] = {}

    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    for num in arr:
        if frequency_map[num] == 1:
            print(num)

    print("HashMap: ", frequency_map)