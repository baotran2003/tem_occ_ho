"""
**Bài 8: Tìm số nguyên dương nhỏ nhất chưa xuất hiện**

**Yêu cầu:**
Cho một mảng gồm `n` phần tử số nguyên (có thể chứa cả số âm và số 0). Hãy tìm số nguyên dương nhỏ nhất (bắt đầu từ `1, 2, 3, ...`) không có mặt trong mảng đã cho.
**Ví dụ:**
* **Đầu vào (Input):** `[2, 3, -1, 1, 5]`
* **Đầu ra (Output):** `4`
"""
def find_first_missing_positive(nums: list[int]) -> int:

    target: int = 1
    # while True:
    #     if target in nums:
    #         target += 1
    #     else:
    #         return target

    # nums.sort()
    # for num in nums:
    #     if num == target:
    #         target += 1
    #     elif num > target:
    #         break
    # return target

    # dung dict
    # freq_map: dict[int, int] = {}
    #
    # for num in nums:
    #     freq_map[num] = 1
    #
    # for _ in range (len(nums)):
    #     if target in freq_map.keys():
    #         target += 1
    #     else:
    #         return target
    #
    # return len(nums) + 1

    # dung set
    nums_set: set[int] = set(nums)

    for _ in range (len(nums)):
        if target in nums_set:
            target += 1
        else:
            return target
    return len(nums) + 1

"""
target = 1 num = 2 -> bo qua
target = 1 num = 3 -> bo
target = 1 num = 1
"""


if __name__ == "__main__":
    input_array = [2, 3, 1, 1, 5]
    input_array_2 = [1, 2, 3,6, 4, 5, 6]
    result = find_first_missing_positive(input_array_2)
    print(f"The smallest positive integer that has not yet appeared is: {result}")