from typing import List

def find_pairs_with_sum(nums: List[int], target: int) -> List[List[int]]:
    result_arr: List[List[int]] = []
    n: int = len(nums)

    for i in range (n):
        for j in range (i + 1, n):
            if nums[i] + nums[j] == target:
                result_arr.append([nums[i], nums[j]])

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [2, 4, 3, 5, 6, -1]
    print(find_pairs_with_sum(test_arr, 5))

