from typing import List

def check_palidrome(nums: List[int]) -> bool:
    n: int = len(nums)
    left: int = 0
    right: int = n - 1

    while left < right:
        if nums[left] == nums[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    nums: List[int] = [1, 2, 5, 2, 1]
    nums1: List[int] = [1, 3, 5, 2, 1]

    print(check_palidrome(nums))