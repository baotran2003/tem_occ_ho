from typing import List, Optional

def find_second_largest(nums: List[int]) -> int:
    # find the largest number
    max_num: int = nums[0]
    n: int = len(nums)
    index: int = 0

    for i in range(n):
        if nums[i] > max_num:
            max_num = nums[i]
            index = i

    second_max= float('-inf')
    for i in range(n):
        if nums[i] > second_max and i != index:
            second_max = nums[i]
    return second_max

if __name__ == "__main__":
    numbers: list[int] = [1, 4, 2, 6, 10,10,  12, 12]
    result: int = find_second_largest(numbers)

    print("The second_largest number is:", result)


