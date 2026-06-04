from typing import List, Optional

def reverse_array(nums: List[int]) -> List[int]:
    n: int = len(nums)
    reverse_arr: List[int] = []
    for i in range(n - 1, -1, -1):
        reverse_arr.append(nums[i])
    return reverse_arr


def is_palindrome(nums: List[int]) -> bool:
    nums2: List[int] = []
    num3: List[int] = []
    n: int = len(nums)

    for i in range(n // 2):
        nums2.append(nums[i])

    # ai
    for i in range(n // 2 + (n % 2), n):
        num3.append(nums[i])

    if nums2 == reverse_array(num3):
        return True

    return False


if __name__ == "__main__":
    print(is_palindrome([1, 2, 3, 2, 1]))
    print(is_palindrome([1, 2, 2, 1]))
    print(is_palindrome([1, 2, 3, 4, 1]))