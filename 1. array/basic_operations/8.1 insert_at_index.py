from typing import List

def insert_at_index (nums: List[int], x: int, k: int) -> list[int]:

    # n: int = len(nums)
    # result_arr: List[int] = []
    #
    # for i in range (n):
    #     if i == k:
    #         result_arr.append(x)
    #     result_arr.append(nums[i])
    #
    # if k == n:
    #     result_arr.append(x)
    #
    # return result_arr

    n: int = len(nums)
    nums.append(0)

    print(n)

    for i in range (n, k, -1):
        nums[i] = nums[i - 1]
        
    nums[k] = x

    return nums


if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 3, 17, 8, 22, 22]  # [1, 5, 3, 17, 8, 22, 22, 0]
    print("array after insert:", insert_at_index(numbers, 10, 3))