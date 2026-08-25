def can_divide_three_parts(a: list[int]) -> bool:
    total_sum: int = sum(a)

    if total_sum % 3 != 0:
        return False

    target: int = total_sum // 3
    current_sum: int = 0
    flag_cut: bool = False

    n = len(a)
    for i in range (n - 1):
        current_sum += a[i]

        # diem cat thu 2
        if current_sum == 2 * target and flag_cut == True:
            return True

        # tim duoc diem cat dau tien
        if current_sum == target:
            flag_cut = True

    return False



if __name__ == "__main__":

    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]

    result = can_divide_three_parts(A)

    if result:
        print("Kết quả: Có thể chia mảng thành 3 phần bằng nhau.")
    else:
        print("Kết quả: Không thể chia.")
