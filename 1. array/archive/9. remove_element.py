from typing import List

def delete_element(nums: List[int], x: int):
    result_arr: List[int] = []

    for num in nums:
        if num != x:
            result_arr.append(num)

    return result_arr

if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 3, 17, 8, 22, 22]
    print("array after remove:", delete_element(numbers, 22))