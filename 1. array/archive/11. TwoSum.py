from typing import List, Tuple
def find_pairs(nums: List[int], target_num: int) -> List[Tuple[int, int]]:
    n: int = len(nums)
    result_arr: List[Tuple[int, int]] = []

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target_num:
                result_arr.append((nums[i], nums[j]))

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [2, 4, 3, 5, 6, -1]
    target_num: int = 5
    print(find_pairs(test_arr, target_num))

    arr_1: Tuple[int, int] = (1, 2)
    arr_1 = (2, 3)

    print(arr_1)
    print(arr_1[0])
    print(arr_1[1])

    arr_1[0] = 12

    arr_2: List[int, int] = [1, 2]