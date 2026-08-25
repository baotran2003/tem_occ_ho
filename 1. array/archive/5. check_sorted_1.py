from typing import List, Optional

def is_ascending(nums: List[int]) -> bool:
    n: int = len(nums)

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

if __name__ == "__main__":
    numbers: list[int] = [1, 3, 5, 2, 10]
    numbers2: list[int] = [1, 3, 5, 7, 10]
    result: bool = is_ascending(numbers)
    print("ascending_array:", result)