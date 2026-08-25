from typing import List

def find_second_largest(nums: List[int]) -> int:
    max: int = nums[0]
    n: int = len(nums)

    for i in range (n):
        if nums[i] > max:
            max = nums[i]

    second_max: int = float("-inf")

    for i in range (n):
        if nums[i] > second_max and nums[i] != max:
            second_max = nums[i]

    return second_max

if __name__ == "__main__":
    numbers: list[int] = [1, 4, 2, 6, 10, 12]
    result: int = find_second_largest(numbers)

    print("The second_largest number is:", result)