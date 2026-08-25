
def merge_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    array_result: list[int] = []
    for num in nums1:
        array_result.append(num)
    for num in nums2:
        array_result.append(num)

    return array_result

def merge_sorted_arrays (nums1: list[int], nums2: list[int]) -> list[int]:
    result_array: list[int] = []
    i: int = 0
    j: int = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result_array.append(nums1[i])
            i += 1
        else:
            result_array.append(nums2[j])
            j += 1

    result_array.extend(nums1[i:])
    result_array.extend(nums2[j:])

    return result_array

if __name__ == "__main__":
    re = []
    a1 = [1, 3, 5]
    a2 = [2, 4, 6]
    print("regular merging:", merge_arrays(a1, a2))

    print("2 sorted arrays: ", merge_sorted_arrays(a1, a2))