"""
12. Tìm số nguyên dương nhỏ nhất chưa xuất hiệnĐề bài: Cho mảng $N$ phần tử (giá trị bất kỳ). Tìm số nguyên dương nhỏ nhất ($1, 2, 3...$) không nằm trong mảng.
"""

def find_first_missing_positive(nums: list[int]) -> int:
    n = len(nums)

    maker_arr = [0] * (n + 1)

    for num in nums:
        if 1 <= num <= n:
            maker_arr[num] = 1

    for i in range (1, n + 1):
        if maker_arr[i] == 0:
            return i

    return n + 1

if __name__ == "__main__":
    # Test 1: Khuyết số ở giữa
    arr1 = [3, 4, -1, 1]  # N = 4, các số hợp lệ là 3 và 1
    print("Array 1:", arr1)
    print("The smallest number has not yet appeared.:", find_first_missing_positive(arr1))

    print("-" * 30)

    # # Test 2: Mảng liên tục từ 1 đến N
    # arr2 = [1, 2, 0]  # N = 3, các số hợp lệ là 1 và 2
    # print("Mảng 2:", arr2)
    # print("The smallest number has not yet appeared.:", find_first_missing_positive(arr2))
    #
    # print("-" * 30)
    #
    # # Test 3: Mảng toàn số to hoặc số âm
    # arr3 = [7, 8, 9, 11, 12]  # N = 5, không có số nào nằm trong khoảng [1, 5]
    # print("Mảng 3:", arr3)
    # print("The smallest number has not yet appeared.:", find_first_missing_positive(arr3))