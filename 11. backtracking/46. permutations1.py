from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        used: List[bool] = n * [False]

        path: List[int] = []

        result: List[List[int]] = []
        self.backtracking(path=path, used=used, nums=nums, n=n, result=result)

        return result

    def backtracking(self, path: List[int], used: List[bool], nums: List[int], n: int, result: List[List[int]]) -> None:
        # Step 1: Base case
        if len(path) == n:
            # result.append(path) -> key
            result.append(path[:])
            return

        # Step 2: backtrack
        for i in range(n):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True
            self.backtracking(path=path, used=used, nums=nums, n=n, result=result)
            used[i] = False
            path.pop()

if __name__ == "__main__":
    nums: List[int] = [1, 2, 3]
    s: Solution = Solution()
    result: List[List[int]] = s.permute(nums)
    print(result)