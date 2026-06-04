from typing import List, Optional

def find_duplicate_brute_force(nums: List[int] ) -> int:
    n: int = len(nums)
    # select the number to check
    for i in range(n):
        # select the number to compare
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]
    return None

if __name__ == "__main__":
    numbers: List[int] = [4, 5, 8, 1, 8, 2]
    result: int = find_duplicate_brute_force(numbers)
    print("The repeated number is:", result)