from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    n: int = len(arr)
    arr.sort()
    min_val = float("inf")
    result_arr: List[List[int]] = []

    for i in range (n - 1):
        val: int = arr[i + 1] - arr[i]
        if val < min_val:
            min_val = val
            result_arr = [[arr[i], arr[i + 1]]]
        elif val == min_val:
            result_arr.append([arr[i], arr[i + 1]])

    return result_arr


if __name__ == "__main__":
    arr1: List[int] = [4, 2, 1, 3]              # [1, 2, 3, 4]
    print(minimumAbsDifference(arr1))

    arr2: List[int] = [1,3,6,10,15]
    print(minimumAbsDifference(arr2))

    arr3: List[int] = [3,8,-10,23,19,-4,-14,27] # [ -14, -10, -4, 3, 8, 19, 23, 27]
    print(minimumAbsDifference(arr3))

    arr4: List[int] = [40, 11, 26, 27, -20]  # [-20, 11, 26, 27, 40]
    print(minimumAbsDifference(arr4))