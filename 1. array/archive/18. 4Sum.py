from typing import List

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n: int = len(nums)
        result: set[tuple[int, int, int, int]] = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen: set[int] = set()
                for k in range(j + 1, n):
                    need: int = target - nums[i] - nums[j] - nums[k]
                    if need in seen:
                        p1, p2, p4, p3 = sorted([nums[i], nums[j], nums[k], need])
                        result.add((p1, p2, p4, p3))
                    seen.add(nums[k])

        return [list(x) for x in result]

if __name__ == "__main__":
    s: Solution = Solution()
    nums: List[int] = [1,0,-1,0,-2,2]
    target: int = 0
    result: List[List[int]] = s.fourSum(nums, target)
    print(result)