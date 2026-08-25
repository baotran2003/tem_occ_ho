# problem 1: Tim vi tri can bang (pivot index)
# Cho mang A gom N phan tu. Tim vi tri i (1 <= i <= N) sao cho
# tong cac phan tu dung truoc i bang tong cac phan tu dung sau i.
# Neu khong co vi tri nao thoa man, in ra -1.
# Vi du: A = [1, 7, 3, 6, 5, 6] -> vi tri 4 (gia tri 6),
#   tong trai 1+7+3 = 11 bang tong phai 5+6 = 11.

if __name__ == "__main__":
    a = [1, 7, 3, 6, 5, 6]
    n: int = len(a)

    pivot_index: int = -1

    for i in range (n):
        left_sum: int = 0
        for j in range (0, i):
            left_sum += a[j]

        right_sum: int = 0
        for j in range (i + 1, n):
            right_sum += a[j]

        if left_sum == right_sum:
            pivot_index = i + 1
            break

    print(pivot_index)

    # CACH 2: DUNG PREFIX_NUM
    # prefix_num: list[int] = [0]
    #
    # current_sum: int = 0
    #
    # for num in a:
    #     current_sum += num
    #     prefix_num.append(current_sum)
    #
    # total_sum = prefix_num[-1]
    # pivot_index: int = -1
    #
    # for i in range (n):
    #     left_sum: int = prefix_num[i]
    #     right_sum: int = total_sum - a[i] - left_sum
    #
    #     if left_sum == right_sum:
    #         pivot_index = i + 1
    #         break
    #
    # print(pivot_index)


# Problem 2: Mang hieu co ban (Difference Array / Range Update)
# Cho mang A gom N phan tu ban dau deu bang 0. Co Q thao tac (L, R, X):
# cong them X vao tat ca cac phan tu tu vi tri L den R (1-based).
# In ra mang cuoi cung sau khi thuc hien het cac thao tac.
#
# Ví dụ:Mảng ban đầu 5 phần tử: [0, 0, 0, 0, 0]
# Thao tác: (2, 4, 3)  Mảng trở thành: [0, 3, 3, 3, 0]

