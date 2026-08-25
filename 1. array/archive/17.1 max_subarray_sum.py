from typing import List

def find_max (nums: List[int]) -> int:
    max_sum = nums[0]
    n: int = len(nums)

    for i in range (n):
        current_sum: int = 0
        for j in range(i, n):
            current_sum += nums[j]

            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

if __name__ == "__main__":

    test_arr: List[int] = [1, -2, 5, 8 ]

    print("Max subarray sum:", find_max(test_arr))