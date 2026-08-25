from typing import List

def remove_duplicate(nums: List[int]) -> List[int]:
    result_arr: List[int] = []
    n: int = len(nums)

    for num in nums:
        # chua xuat hien add vao mang
        if num not in result_arr:
            result_arr.append(num)

    return result_arr

if __name__ == "__main__":
    test_arr: List[int] = [1, 2, 2, 3, 4, 4, 1, 5]
    print(remove_duplicate(test_arr))