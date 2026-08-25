from typing import List

def find_duplicate_brute_force(nums: List[int]) -> List[int]:
    result_arr: List[int] = []
    n: int = len(nums)
    for i in range (n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                result_arr.append(i)

    return result_arr

if __name__ == "__main__":
    numbers: List[int] = [4, 5, 8, 8, 8, 2, 2]
    result: List[int] = find_duplicate_brute_force(numbers)
    print("The repeated number is:", result)