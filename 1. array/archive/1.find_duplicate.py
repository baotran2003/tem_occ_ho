from typing import List

def find_duplicate_brute_force(nums: List[int] ) -> List[int]:
    n: int = len(nums)
    new_arr: List[int] = []
    # select the number to check
    for i in range(n):
        # select the number to compare
        for j in range(i + 1, n) :
            if nums[i] == nums[j] and nums[i] not in new_arr:
                new_arr.append(nums[i])
    return new_arr


if __name__ == "__main__":
    numbers: List[int] = [4, 5, 8, 1, 8, 2, 2, 8]
    result: list[int] = find_duplicate_brute_force(numbers)
    print("The repeated number is:", result)