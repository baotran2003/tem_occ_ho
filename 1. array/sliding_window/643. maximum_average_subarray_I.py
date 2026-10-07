from typing import List
# Sliding Window cố định (Fixed Size)

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # current_sum: int = 0
        #
        # for i in range(k):
        #     current_sum += nums[i]
        #
        # max_sum: int = current_sum
        #
        # for right in range(k, len(nums)):
        #     current_sum += nums[right] - nums[right - k]
        #
        #     if current_sum > max_sum:
        #         max_sum = current_sum
        # return max_sum / k

        # truot het
        current_sum: int = 0
        max_sum: float = float('-inf')
        left: int = 0
        right: int = 0

        while right < len(nums):
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum= max(current_sum, max_sum)
                current_sum -= nums[left]
                left += 1
            right += 1
        return max_sum / k


if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [1, 12, -5, -6, 50, 3]
    k: int = 4

    print(so.findMaxAverage(nums, k))