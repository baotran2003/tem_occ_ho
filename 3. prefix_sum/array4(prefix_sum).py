if __name__ == "__main__":
    arr: list[int] = [1, 5, 3, 0, 8, 8, 9, 9]

    # tinh tong tu i -> j (2, 5)


    i: int = 2 ; j: int = 5
    prefix_sum: list[int] = []
    prefix_sum.append(0)

    current_sum: int = 0

    for num in arr:
        current_sum += num
        prefix_sum.append(current_sum) #        [0, 1, 6, 9, 9, 17, 25, 34, 43]
                                       # index  0  1  2  3  4   5   6   7   8

    result = prefix_sum[j + 1] - prefix_sum[i]
    print(result)
