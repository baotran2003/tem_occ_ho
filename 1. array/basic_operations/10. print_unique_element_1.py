from typing import List, Dict

def print_unique(nums: list[int]) -> List[int]:
    # Cach 1: use .count()
    # result_arr: List[int] = []
    # for num in nums:
    #     if nums.count(num) == 1:
    #         result_arr.append(num)
    # return result_arr


    # cach 2:
    # max_nums: int = max(nums)
    # marker_arr: List[int] = [0] * (max_nums + 1)
    #
    # for num in nums:
    #     marker_arr[num] += 1
    #
    # result_arr: List[int] = []
    # for num in nums:
    #     if marker_arr[num] == 1:
    #         result_arr.append(num)
    #
    # return result_arr

    # cach 3
    freq_map: dict[int, int] = {}
    for num in nums:
        # if num not in freq_map:
        #     freq_map[num] = 1
        # else:
        #     freq_map[num] += 1
        freq_map[num] = freq_map.get(num, 0) + 1

    result_arr: List[int] = []
    for num in nums:
        if freq_map[num] == 1:
            result_arr.append(num)

    return result_arr
if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 5, 3, 17, 8, 22, 22]
    print("unique_element:", print_unique(numbers))