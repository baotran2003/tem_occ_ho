from typing import List

#Two pointers
def is_palindrome(nums: List[int]) -> bool:
    n: int = len(nums)

    left: int = 0
    right: int = n - 1

    while left < right:
        if nums[left] != nums[right]:
            return False

        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome([1, 2, 3, 2, 1]))
    print(is_palindrome([1, 2, 2, 1]))
    print(is_palindrome([1, 2, 3, 4, 1]))