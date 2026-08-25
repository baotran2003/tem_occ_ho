from typing import List

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # n: int = len(nums)
        # pivot_index: int = -1
        # for i in range(n):
        #     left_sum: int = 0
        #     for j in range(0, i):
        #         left_sum += nums[j]
        #
        #     right_sum: int = 0
        #     for j in range(i + 1, n):
        #         right_sum += nums[j]
        #
        #     if left_sum == right_sum:
        #         pivot_index = i
        #         break
        # return pivot_index
        prefix_sum: List[int] = [0]
        current_sum: int = 0
        n: int = len(nums)

        for num in nums:
            current_sum += num
            prefix_sum.append(current_sum)

        total_sum: int = prefix_sum[-1]
        for i in range(n):
            left_sum: int = prefix_sum[i]
            right_sum: int = total_sum - nums[i] - left_sum

            if left_sum == right_sum:
                return i
        return -1



if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 7, 3, 6, 5, 6]
    print(f"Input: {nums1}")
    print(f"Pivot Index: {sol.pivotIndex(nums1)}\n")  # Expected: 3

    # Test case 2
    nums2 = [1, 2, 3]
    print(f"Input: {nums2}")
    print(f"Pivot Index: {sol.pivotIndex(nums2)}\n")  # Expected: -1

    # Test case 3
    nums3 = [2, 1, -1]
    print(f"Input: {nums3}")
    print(f"Pivot Index: {sol.pivotIndex(nums3)}")  # Expected: 0