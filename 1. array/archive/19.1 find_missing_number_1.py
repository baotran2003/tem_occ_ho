from typing import List

def find_miss_number(nums: List[int], n: int) -> int:
    expected_num = n * (n + 1) // 2
    actual_num: int = 0

    for num in nums:
        actual_num += num

    return expected_num - actual_num

if __name__ == "__main__":
    # Ví dụ: n = 5, mảng đáng lẽ từ 1 đến 5 nhưng bị thiếu mất số 4
    test_arr: List[int] = [1, 2, 5, 3]
    n_elements: int = 5

    print("The number missing:", find_miss_number(test_arr, n_elements))