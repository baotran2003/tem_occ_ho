from typing import List

def rearrange_negatives(nums: List[int]) -> List[int]:
    left: int = 0
    right: int = len(nums) - 1

    while left < right:
        if nums[left] < 0:
            left += 1
        elif nums[right] > 0:
            right -= 1
        else:
            nums[left], nums[right] =  nums[right], nums[left]
            left += 1
            right -= 1

    return nums

if __name__ == "__main__":
    test_arr: List[int] = [12, -1, 3, -5, 6, -7, 5, -3]
    print("Kết quả giữ nguyên thứ tự:")
    print(rearrange_negatives(test_arr))