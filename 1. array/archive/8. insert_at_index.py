from typing import List

def insert_at_index(nums: list[int], x: int, k: int) -> List[int]:
    result_arr: List[int] = []
    n: int = len(nums)

    for i in range(n):
        if i == k:
            result_arr.append(x)
        result_arr.append(nums[i])

    if k == n:
        result_arr.append(x)

    return result_arr

if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 3, 17, 8, 22, 22]
    print("array after insert:", insert_at_index(numbers, 10, 3))
