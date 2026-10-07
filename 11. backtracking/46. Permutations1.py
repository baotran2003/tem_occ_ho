from typing import List
# hoan vi - chinh hop

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path: List[int] = []
        result: List[List[int]] = []
        n: int = len(nums)

        used: List[bool] = n * [False]

        self.backtracking(n=n, used=used, path=path, nums=nums, result=result)

        return result

    def backtracking(self, n: int, used: List[bool], path: List[int], nums: List[int], result: List[List[int]]) -> None:
        # Base Case
        if len(path) == n:
            result.append(path[:])
            return

        for i in range (3):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True

            self.backtracking(n=n, used=used, path=path, nums=nums, result=result)

            used[i] = False
            path.pop()


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3]
    s: Solution = Solution()
    result: List[List[int]] = s.permute(nums)
    print(result)