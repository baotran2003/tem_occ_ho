from typing import  List


class Solution:
    def removeDuplicates(self, nums: List[int], val: int) -> int:
        result_arr: List[int] = [nums[0]]
        n: int = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                result_arr.append(nums[i])

        for i in range (len(result_arr)):
            nums[i] = result_arr[i]

        return len(result_arr)


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    st: Solution = Solution()
    print(st.removeElement(nums, val))