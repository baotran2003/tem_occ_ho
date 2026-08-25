from typing import List, Tuple

def find_pairs_with_sum(nums: List[int], target: int) -> List[Tuple[int, int]]:
    result_arr: List[Tuple[int, int]] = []
    n: int = len(nums)

    # for i in range (n):
    #     for j in range (i + 1, n):
    #         if nums[i] + nums[j] == target:
    #             result_arr.append([nums[i], nums[j]])
    #
    # return result_arr

    seen_map: dict[int, int] = {}


    for i in range (n):
        complement: int = target - nums[i]
        if complement in seen_map:
            result_arr.append((seen_map[complement], i))
        seen_map[nums[i]] = i

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [2, 4, 3, 5, 6, -1]
    print(find_pairs_with_sum(test_arr, 5))

