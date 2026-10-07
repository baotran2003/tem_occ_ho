from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path: List[int] = []
        result: List[List[int]] = []
        n: int = len(nums)

        self.backtracking(start=0, n=n, nums=nums, path=path, result=result)

        return result

    def backtracking(self, start: int, n: int, nums: List[int], path: List[int], result: List[List[int]]) -> None:
        # Base case
        if start == n:
            result.append(path[:])
            return

        # chia ra 2 nhanh, chon hoac ko chon
        for i in range(2):
            if i == 0:  # ko chon nums[start] vao tap con -> di tiep
                self.backtracking(start=start + 1, n=n, nums=nums, path=path, result=result)
            else:  # chon nums[start] vao tap con -> them vao path -> di tiep -> pop
                path.append(nums[start])
                self.backtracking(start=start + 1, n=n, nums=nums, path=path, result=result)
                path.pop()


if __name__ == "__main__":
    nums: List[int] = [1, 2]
    s: Solution = Solution()
    result: List[List[int]] = s.subsetsWithDup(nums)
    print(result)
