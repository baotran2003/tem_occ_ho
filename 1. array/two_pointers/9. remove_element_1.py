from typing import List

def delete_element(nums: List[int], x: int):
    # result_arr: List[int] = []
    # for num in nums:
    #     if num != x:
    #         result_arr.append(num)
    # return result_arr

    n: int = len(nums)

    # for i in range (n - 1, -1, -1):
    #     if nums[i] == x:
    #         nums.pop()
    #
    # return nums


    point_write: int = 0
    for read in range (n):
        if nums[read] != x:
            nums[point_write] = nums[read]
            point_write += 1

    while len(nums) > point_write:
        nums.pop()

    return nums



if __name__ == "__main__":
    numbers: list[int] = [1, 22, 5, 22, 3]
    print("array after remove:", delete_element(numbers, 22))