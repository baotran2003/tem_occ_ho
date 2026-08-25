from typing import List

def reverse_array(nums: List[int]) -> List[int]:
    # start - step - stop
    result_arr: List[int] = []
    n: int = len(nums)

    for i in range (n - 1, -1, -1):
        result_arr.append(nums[i])

    return result_arr


if __name__ == "__main__":
    numbers: list[int] = [1, 3, 5, 2, 10]
    result: list[int] = reverse_array(numbers)
    print("reverse_array:", result)