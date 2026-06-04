from typing import List, Optional

def reverse_array(nums: list[int]) -> list[int]:
    n: int = len(nums)
    reverse_arr: list[int] = []

    #start - step - stop
    for i in range(n-1, -1, -1):
        reverse_arr.append(nums[i])
    return reverse_arr

if __name__ == "__main__":
    numbers: list[int] = [1, 3, 5, 2, 10]
    result: list[int] = reverse_array(numbers)
    print("reverse_array:", result)