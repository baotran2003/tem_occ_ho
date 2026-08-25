from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    n: int = len(nums)

    for i in range(n):
        min_idx: int = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

if __name__ == "__main__":
    nums: List[int] = [1, 3, 2, 7, 5, 9, 4, 6, 8]
    print(selection_sort(nums))