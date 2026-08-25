from typing import List

def rearrange_negatives(nums: List[int]) -> List[int]:
    result_arr: List[int] = []

    for num in nums:
        if num < 0:
            result_arr.append(num)

    for num in nums:
        if num >= 0:
            result_arr.append(num)

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [12, -1, 3, -5, 6, -7, 5, -3, -6]
    print("Kết quả giữ nguyên thứ tự:")
    print(rearrange_negatives(test_arr))