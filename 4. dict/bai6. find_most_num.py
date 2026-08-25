if __name__ == "__main__":
    arr: list[int] = [1, 5, 3, 0, 8, 8, 9, 9]

    freq_map: dict[int, int] = {}

    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    print("HashMap: ", freq_map)

    for num in freq_map:
        if freq_map[num] == 1:
            print(num)


