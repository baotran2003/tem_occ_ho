from typing import List

def find_difference_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    result_arr: list[int] = []

    for num in arr1:
        if num not in arr2:
            result_arr.append(num)
    return result_arr


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 1]
    b = [2, 4, 6]

    # Các số có trong a nhưng không có trong b là: 1, 3, 5
    print("Elements in a not b:", find_difference_elements(a, b))
    # Kết quả: [1, 3, 5]