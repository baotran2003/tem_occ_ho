if __name__ == "__main__":
    result_arr: list[int] = []

    arr1: list[int] = [4, 1, 8, 4 , 5]
    arr2: list[int] = [5, 6, 1, 8, 4, 5]

    for num in arr1:
        if num in arr2 and num not in result_arr:
                result_arr.append(num)

    print(result_arr)