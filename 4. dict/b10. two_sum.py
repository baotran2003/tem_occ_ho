if __name__ == "__main__":
    arr: list[int] = [0, 1, 2, 3, 5]
    target: int = 5
    n: int = len(arr)

    result_arr: list[list[int]] = []

    seen_dict: dict[int, int] = {}
    for i in range (n):
        complement: int = target - arr[i]
        if complement in seen_dict:
            result_arr.append([seen_dict[complement], i])
        seen_dict[arr[i]] = i


    print(result_arr)  # Output: [[0, 4], [2, 3]]