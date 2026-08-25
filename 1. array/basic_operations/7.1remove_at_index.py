from typing import List


def delete_at_index(nums: List[int], k: int) -> List[int]:
    # n: int = len(nums)
    # result_arr: List[int] = []
    #
    # for i in range(n):
    #     if i == k:
    #         continue
    #     result_arr.append(nums[i])
    #
    # return result_arr

    n: int = len(nums)
    for i in range (k, n - 1):
        nums[i] = nums[i + 1]

    nums.pop()

    return nums



if __name__ == "__main__":
    numbers: list[int] = [1, 5, 3, 17, 8, 22, 22]
    print("new_array:", delete_at_index(numbers, 2))
