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

    # for i in range (n):
    #     left_sum:int = 0

    #     for j in range(0, i):
    #         left_sum += a[j]
    #
    #     right_sum: int = 0
    #     for j in range (i + 1, n):
    #         right_sum += a[j]
    #
    #     if left_sum == right_sum:
    #         pivot_index = i + 1
    #         break
    # print(pivot_index)


    prefix_sum: list[int] = [0]         #-> [0, 1, 8, 11, 17, 22, 28]
    current_sum: int = 0

    for num in a:
        current_sum += num
        prefix_sum.append(current_sum)

    print(prefix_sum)

    total_sum: int = prefix_sum[-1]

    for i in range (n):
        left_sum: int = prefix_sum[i]
        right_sum: int =total_sum - a[i] - left_sum
        
        if left_sum == right_sum:
            pivot_index = i + 1
            break
    print("pivot_index: ", pivot_index)