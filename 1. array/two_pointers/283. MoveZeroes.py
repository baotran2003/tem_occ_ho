from typing import List

class Solution:
    def moveZeroes(self, nums: list[int]) -> tuple[list[int], int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        k: int = 0
        for i in range (0, len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range (k, len(nums)):
            nums[i] = 0


        return nums, k

if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [0, 1, 0, 3, 12]
    print(so.moveZeroes(nums))