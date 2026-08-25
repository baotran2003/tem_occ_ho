from typing import List

def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    result_arr: List[int] = []
    for num in arr1:
        result_arr.append(num)

    for num in arr2:
        result_arr.append(num)

    return result_arr

# gop 2 mang sap xep
def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    combine_arr: List[int] = merge_arrays(arr1, arr2)
    n: int = len(combine_arr)

    # for i in range (n):
    #     for j in range (i + 1, n):
    #         if combine_arr[j] < combine_arr[i]:
    #             combine_arr[i], combine_arr[j] = combine_arr[j], combine_arr[i]
    # return combine_arr

    result_arr: List[int] = []
    i: int = 0
    j: int = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result_arr.append(arr1[i])
            i += 1
        else:
            result_arr.append(arr2[j])
            j += 1

    result_arr.extend(arr1[i:])
    result_arr.extend(arr2[j:])
    return result_arr


if __name__ == "__main__":
    a1 = [1, 3, 5]
    a2 = [2, 4, 6]
    print("1. regular merging:", merge_arrays(a1, a2))

    print("2. sorted arrays: ", merge_sorted_arrays(a1, a2))