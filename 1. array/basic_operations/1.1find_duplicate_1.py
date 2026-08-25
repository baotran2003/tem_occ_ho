from typing import List

def find_duplicate_brute_force(nums: List[int]) -> List[int]:
    result_arr: List[int] = []
    n: int = len(nums)
    freq_map: dict[int, int] = {}

    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    for num, count in freq_map.items():
        if count > 1:
            result_arr.append(num)

    # for i in range (n):
    #     for j in range (i + 1, n):
    #         if nums[i] == nums[j] and nums[i] not in result_arr:
    #             result_arr.append(nums[i])

    return result_arr

if __name__ == "__main__":
    numbers: List[int] = [4, 5, 8, 8, 8, 2, 2]
    result: List[int] = find_duplicate_brute_force(numbers)
    print("The repeated number is:", result)