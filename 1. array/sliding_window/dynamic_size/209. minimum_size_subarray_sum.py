from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left: int = 0
        result: float = float('inf')
        total: int = 0

        for right in range (len(nums)):
            total += nums[right]
            # thu nho left cho den khi < target
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        return result if result != float("inf") else 0


if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [2,3,1,2,4,3] # 2: [4, 3]
    target: int = 7
    print(so.minSubArrayLen(target, nums))