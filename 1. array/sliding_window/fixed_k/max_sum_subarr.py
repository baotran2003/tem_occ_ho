class Solution:
    def maxSumSubArr(self, nums: list[int], k: int) -> float:
        current_sum: int = 0
        max_sum: float = float('-inf')
        left: int = 0

        # # first window
        # for i in range(k):
        #     current_sum += nums[i]
        # max_sum: int = current_sum
        # # sliding
        # for right in range(k, len(nums)):
        #     left: int = right - k
        #     current_sum += nums[right] - nums[left]
        #     max_sum = max(max_sum, current_sum)
        # return max_sum

        for right in range(len(nums)):
            current_sum += right

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                current_sum -= nums[left]
                left += 1
        return max_sum


if __name__ == "__main__":
    so: Solution = Solution()
    nums: list[int] = [4, 1, 2, 4, 3, 2, 5,]
    k: int = 4
    print(so.maxSumSubArr(nums, k))