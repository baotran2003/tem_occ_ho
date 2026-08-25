from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    n: int = len(nums)

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if nums[j] > nums[i]:
    #             for k in range(j + 1, n):
    #                 if nums[k] > nums[j]:
    #                     return True
    # return False

    # Khởi tạo 2 biến đại diện cho số thứ nhất và số thứ hai bằng vô cùng lớn
    first = float('inf')
    second = float('inf')
    n: int = len(nums)
    

    for num in range(n):  # Lấy giá trị của từng số trong mảng
        val = nums[num]

        if val <= first:
            first = val  # Tìm thấy số nhỏ nhất mới
        elif val <= second:
            second = val  # Tìm thấy số vừa nhỏ nhất mới (chắc chắn > first)
        else:
            # Nếu số hiện tại lớn hơn cả second -> Đã tìm thấy số thứ ba thỏa mãn!
            return True

    return False



if __name__ == "__main__":
    # nums1: List[int] = [1,2,3,4,5]
    # print("Output: ", increasingTriplet(nums1))
    #
    # nums2: List[int] = [5,4,3,2,1]
    # print("Output: ", increasingTriplet(nums1))

    nums1: List[int] = [2,1,5,0,4,6]
    print("Output: ", increasingTriplet(nums1))