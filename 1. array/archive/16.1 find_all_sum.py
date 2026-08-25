from typing import List

def find_pairs_with_sum(nums: list[int], target: int) -> List[List[int]]:
    result_arr: List[List[int]] = []
    seen_set: set = set()

    for num in nums:
        complement = target - num

        if complement in seen_set:
            result_arr.append([complement, num])

        seen_set.add(num)

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [2, 4, 3, 5, 6, -1]
    print(find_pairs_with_sum(test_arr, 5))