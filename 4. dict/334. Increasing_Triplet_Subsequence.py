from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    # n: int = len(nums)
    # for i in range(n):
    #     for j in range (i + 1, n):
    #         if nums[j] > nums[i]:
    #             for k in range (j + 1, n):
    #                 if nums[k] > nums[j]:
    #                     return True
    # return False

    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False


if __name__ == "__main__":
    # nums1: List[int] = [1,2,3,4,5]
    # print("Output: ", increasingTriplet(nums1))
    #
    nums2: List[int] = [3, 4, 1, 5]
    print("Output: ", increasingTriplet(nums2))

    nums1: List[int] = [2,1,5,0,4,6]
    print("Output: ", increasingTriplet(nums1))