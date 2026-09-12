from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []
        n: int = len(nums)

        self.backtracking(start=0, n=n, nums=nums, path=path, result=result)

        return result

    def backtracking(self, start: int, n: int, nums: List[int], path: List[int], result: List[List[int]]) -> None:
        # Base case
        if start == n:
            result.append(path[:])
            return  # quay ve backtracking(start = start - 1, ...)

        for i in range(2):
            if i == 0:  # khong chon nums[start] vao tap con -> di tiep phan tu tiep theo
                self.backtracking(start=start + 1, n=n, nums=nums, path=path, result=result)
            else:  # chon nums[start] vao tap con -> them vao path -> di tiep -> pop
                path.append(nums[i])
                self.backtracking(start=start + 1, n=n, nums=nums, path=path, result=result)
                path.pop()








if __name__ == "__main__":
    nums: List[int] = [1, 2]
    s: Solution = Solution()
    result: List[List[int]] = s.subsets(nums)
    print(result)
