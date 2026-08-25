if __name__ == "__main__":
    arr: list[int] = [1, 5, 3, 0, 8, 8, 9, 9]

    # 0 1 2 3 4 5 6 7 8 9 - Gia tri
    # 1 1 0 1 0 1 0 0 2 2 - So Lan xuat hien

    # Input: 6 và mảng  arr = [1, 2, 3, 3, 2, 5, 1, 2, 100000]

    # danh_dau[1] = 2
    # danh_dau[2] = 3
    # danh_dau[3] = 2
    # danh_dau[5] = 1
    # danh_dau[100000] = 1

    marker_arr: list[int] = [0] * (max(arr) + 1)

    for num in arr:
        marker_arr[num] += 1

    for num in arr:
        if marker_arr[num] == 1:
            print(num)