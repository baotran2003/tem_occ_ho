
# tinh tong tu i -> j (2, 5) 3+ 0 + 8 + 8
if __name__ == "__main__":
    arr: list[int] = [1, 5, 3, 0, 8, 8, 9, 9]
    i: int = 2
    j: int = 5
    current_sum: int = 0
    # sum[i] = a0 + a1 +... + a[i - 1]
    # sum[j + 1] = a0 + a1 +... + a[i- 1] + a[i] +...+ a[j]

    prefix_sum: list[int] = [0]     # [0, 1, 6, 9, 9, 17, 25, 34]
    for num in arr:
        current_sum += num
        prefix_sum.append(current_sum)

    print(prefix_sum[j + 1] - prefix_sum[i])



