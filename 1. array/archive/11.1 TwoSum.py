from typing import List, Tuple

def find_pairs(nums: List[int], target: int) -> List[int]:
    n: int = len(nums)

    seen_map: dict[int, int] = {}

    for i in range (n):
        complement: int = target - nums[i]
        if complement in seen_map:
            return [seen_map[complement], i]

        seen_map[nums[i]] = i

    return []


if __name__ == "__main__":
    test_arr: List[int] = [2, 4, 3, 5, 6, -1]
    target_num: int = 5
    print(find_pairs(test_arr, target_num))

