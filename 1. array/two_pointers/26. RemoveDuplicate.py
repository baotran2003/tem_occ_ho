from  typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # temp: List[int] = [nums[0]]
        #
        # for i in range (1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         temp.append(nums[i])
        #
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        #
        # return len(temp)

        # Slow & Fast
        slow: int = 0

        for fast in range (1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

if __name__ == "__main__":
    so: Solution = Solution()
    nums: List[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    print(so.removeDuplicates(nums))