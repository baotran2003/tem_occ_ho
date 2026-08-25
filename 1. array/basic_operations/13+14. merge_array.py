from typing import List

def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    result_arr: List[int] = []

    for num1 in arr1:
        result_arr.append(num1)

    for num2 in arr2:
        result_arr.append(num2)

    return result_arr

# gop 2 mang sap xep
def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    combine_arr: List[int] = merge_arrays(arr1, arr2)
    n: int = len(combine_arr)

    # so sanh i voi tat ca ptu sau <=> Selection sort
    # for i in range (n):
    #     for j in range(i + 1, n):
    #         if combine_arr[i] > combine_arr[j]:
    #             combine_arr[i], combine_arr[j] = combine_arr[j], combine_arr[i]

    # Buble sort - so sanh 2 ptu lien ke
    for i in range (n):
        for j in range (0, n - i - 1):
            if combine_arr[j] > combine_arr[j + 1]:
                temp: int = combine_arr[j]
                combine_arr[j] = combine_arr[j + 1]
                combine_arr[j + 1] = temp

    return combine_arr


if __name__ == "__main__":
    re = []
    a1 = [1, 3, 5]
    a2 = [2, 4, 6]
    print("regular merging:", merge_arrays(a1, a2))

    print("2 sorted arrays: ", merge_sorted_arrays(a1, a2))