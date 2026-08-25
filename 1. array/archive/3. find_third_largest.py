from typing import List, Optional

def find_third_largest(nums: List[int]) -> int:
    nums.sort()
    
    # find the largest number
    max1: int = nums[0]
    n: int = len(nums)

    for i in range(n):
        if nums[i] > max1:
            max1 = nums[i]

    max2= float('-inf')
    for i in range(n):
        if nums[i] > max2 and nums[i] != max1:
            max2 = nums[i]

    max3 = float('-inf')
    for i in range(n):
        if nums[i] > max3 and nums[i] != max1 :
            max3 = nums[i]
    return max3

if __name__ == "__main__":
    numbers: list[int] = [1, 4, 2, 6, 10, 10, 12, 12, 12]
    result: int = find_third_largest(numbers)

    print("The third_largest number is:", result)


