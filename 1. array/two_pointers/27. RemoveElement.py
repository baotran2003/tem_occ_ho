from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # for i in range (n - 1, -1, -1):
        #     if nums[i] == x:
        #         nums.pop()
        #
        # return nums

        # fast & slow point
        n: int = len(nums)
        count: int = 0

        for i in range(n):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        return count

if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [1, 1, 1, 1]
    val: int = 1
    print(so.removeElement(nums, val))