from typing import List

def rotate_left_once(nums: List[int]) -> List[int]:
    first_element: int = nums[0]
    n: int = len(nums)

    for i in range (n - 1):
        nums[i] = nums[i + 1]

    nums[n - 1] = first_element

    return nums


def rotate_right_once(nums:List[int]) -> List[int]:
    n: int = len(nums)
    first_element: int = nums[n - 1]

    # start - stop - step
    for i in range (n - 1, 0, -1):
        nums[i] = nums[i - 1]

    nums[0] = first_element

    return nums

def rotate_left_k_times(nums: List[int], k: int) -> List[int]:
    n: int = len(nums)
    f: int = k % n
    result_arr: List[int] = []

    for i in range(k, n):
        result_arr.append(nums[i])

    for i in range(0, k):
        result_arr.append(nums[i])

    return result_arr

# k % n


if __name__ == "__main__":

    origin_arr = [10, 20, 30, 40, 50]
    # i = 0 nums[0] = nums[1] => nums[0] = 20 -> [20, 20, 30, 40, 50]
    # i = 1 nums[1] = nums[2] => nums[1] = 30 -> [20, 30, 30, 40, 50]
    # i = 2 nums[2] = nums[3] => nums[2] = 40 -> [20. 30, 40, 40, 50]
    # i = 3 nums[3] = nums[4] => nums[3] = 50 -> [20 30 40 50 50]

    print("Mảng gốc:      ", origin_arr)
    print("Switch left once:", rotate_left_once(list(origin_arr)))  # [20, 30, 40, 50, 10]
    print("Switch right once:", rotate_right_once(list(origin_arr))) # [50, 10, 20, 30, 40]
    print("Switch left twice", rotate_left_k_times(list(origin_arr), 2)) # [30, 40, 50, 10, 20]

    # k = 1000,     (i+k) % n