"""
**Bài 8: Tìm số nguyên dương nhỏ nhất chưa xuất hiện**

**Yêu cầu:**
Cho một mảng gồm `n` phần tử số nguyên (có thể chứa cả số âm và số 0). Hãy tìm số nguyên dương nhỏ nhất (bắt đầu từ `1, 2, 3, ...`) không có mặt trong mảng đã cho.
**Ví dụ:**
* **Đầu vào (Input):** `[2, 3, -1, 1, 5]`
* **Đầu ra (Output):** `4`
"""
def find_first_missing_positive(nums: list[int]) -> int:

    # n: int = len(nums)
    #
    # target: int = 1
    # while True:
    #     if target in input_array:
    #         target += 1
    #     else:
    #         return target
    max_nums: int = max(nums)
    marker_arr: list[int] = [0] * (max_nums + 1)

    for num in nums:
        marker_arr[num] = 1

    for i in range (1, len(marker_arr)):
        if marker_arr[i] == 0:
            return i

    return len(nums) + 1



"""
target = 1 num = 2 -> bo qua
target = 1 num = 3 -> bo
target = 1 num = 1
"""


if __name__ == "__main__":
    input_array = [2, 3, 1, 1, 5]
    input_array_2 = [1, 2, 3,6, 4, 5, 6]
    result = find_first_missing_positive(input_array)
    print(f"The smallest positive integer that has not yet appeared is: {result}")