from typing import List

def sum_list(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_list(nums[1:])

if __name__ == "__main__":
    my_list: List[int] = [1, 2, 3, 4, 5]
    print(sum_list(my_list))