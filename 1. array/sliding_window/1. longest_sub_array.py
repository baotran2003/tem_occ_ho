from typing import List

class Solution:
    def longestSubArray(self, nums: List) -> int:
        left: int = 0
        right: int = 0
        result: int = 0
        count: int = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                count += 1
                result = max(count, result)
                right += 1
            else:
                left = right
                count = 0

        # for right in range (len(nums)):
        #     if nums[left] == nums[right]:
        #         count += 1
        #     else:
        #         left = right
        #         count = 1
        #     result = max(result, count)
        # return result

        # for right in range (len(nums)):
        #     if nums[left] != nums[right]:
        #         left = right
        #     result = max (result, right - left + 1)

        return result

if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [7, 3, 3, 3, 2, 2, 2, 2]
    print(so.longestSubArray(nums))