def find_intersection_with_set(nums1: list[int], nums2: list[int]) -> list[int]:
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    intersection_set = set_nums1.intersection(set_nums2)
    return list(intersection_set)

def find_intersection_with_dict(nums1: list[int], nums2: list[int]) -> list[int]:
    marker_dict: dict[int, int] = {}

    for num in nums1:
        marker_dict[num] = marker_dict.get(num, 0 ) + 1

    result_arr: list[int] = []

    print(marker_dict)

    # 1: 1, 2: 2, 3: 1
    #buoc 2 result_arr = [2]
    # marker_dict = 1: 1, 2: 1, 3: 1

    # buoc 3 result_arr = [2, 2]
    # marker_dict = 1: 1, 2: 0, 3: 1
    # buoc 4 result_arr = [2, 2]
    # marker_dict = 1: 1, 2: 0, 3: 1

    for num in nums2:
        if num in marker_dict and marker_dict[num] > 0:
            result_arr.append(num)
            marker_dict[num] = marker_dict[num] - 1

    return result_arr

if __name__ == "__main__":
    A = [1, 2, 2, 3]
    B = [2, 2, 2, 3, 5]

    print(find_intersection_with_dict(A, B))