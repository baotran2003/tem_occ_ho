from typing import List
# Sliding Window cố định (Fixed Size)

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 2 for O(n^2)
        # max_sum: int = float('-inf')
        #
        # for i in range(len(nums) - k + 1):
        #     current_sum: int = 0
        #     for j in range(i, k + i):
        #         current_sum += nums[j]
        #     max_sum = max(current_sum, max_sum)
        # return max_sum / k

        # prefix_sum
        prefix_sum: List[int] = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # find all windows of size k gia su 3 windows
        max_sum: int = float('-inf')
        for i in range(len(nums) - k + 1):
            current_sum: int = prefix_sum[i + k] - prefix_sum[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k


        # truot het
        # current_sum: int = 0
        # max_sum: float = float('-inf')
        # left: int = 0
        # right: int = 0
        #
        # while right < len(nums):
        #     current_sum += nums[right]
        #
        #     if right - left + 1 == k:
        #         max_sum= max(current_sum, max_sum)
        #         current_sum -= nums[left]
        #         left += 1
        #     right += 1
        # return max_sum / k


if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [1, 12, -5, -6, 50, 3]
    k: int = 4

    print(so.findMaxAverage(nums, k))