from typing import List

def move_zeroes(nums: List[int]) -> List[int]:
    result_arr: List[int] = []
    for num in nums:
        if num != 0:
            result_arr.append(num)

    count_zero: int = len(nums) - len(result_arr)

    for _ in range (count_zero):
        result_arr.append(0)

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [0, 1, 0, 3, 12, 0, 5]
    print("Kết quả (Mảng mới):", move_zeroes(test_arr))
