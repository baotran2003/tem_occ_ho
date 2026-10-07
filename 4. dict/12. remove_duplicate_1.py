from typing import List

def remove_duplicate(nums: List[int]) -> List[int]:
    result_arr: List[int] = []
    # n: int = len(nums)
    #
    # for num in nums:
    #     if num not in result_arr:
    #         result_arr.append(num)
    # return result_arr

    # cach 2:
    # max_num: int = max(nums)
    # marker_arr: List[int] = [0] * (max_num + 1)
    #
    # for num in nums:
    #     if marker_arr[num] == 0:
    #         result_arr.append(num)
    #         marker_arr[num] = 1
    #
    # return result_arr

    # cach 3:
    freq_map: dict[int, int] = {}

    # moi so xuat hien 1 lan trong ket qua bat ke no xuat hien bao nhieu lan trong mang -> bai toan: da them so nay vao ket qua ?
    for num in nums:
        if num not in freq_map:
            result_arr.append(num)
            freq_map[num] = 1   # danh dau da xuat hien ???

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [1, 2, 2, 3, 4, 4, 1, 5]
    print(remove_duplicate(test_arr))