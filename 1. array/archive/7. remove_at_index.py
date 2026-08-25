from typing import List

def delete_at_index(nums: List[int], k: int) -> List[int]:
    n: int = len(nums)
    nums2: List[int] = []

    for i in range(n):
        if i == k:
            continue
        nums2.append(nums[i])

    return nums2


if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 3, 17, 8, 22, 22]
    print("new_array:", delete_at_index(numbers, 2))