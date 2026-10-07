from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solution 2: Sort + pruning
        candidates.sort()
        path: List[int] = []
        result: List[List[int]] = []

        self.backtracking2(idx=0, curr_sum=0, path=path, candidates=candidates, target=target, result=result)

        return result

    def backtracking2(self, idx: int, curr_sum: int, path: List[int], candidates: List[int], target: int,
                      result: List[List[int]]) -> None:
        if curr_sum == target:
            result.append(path[:])
            return

        for i in range(idx, len(candidates)):
            can = candidates[i]

            if curr_sum + can > target:
                break

            path.append(can)
            self.backtracking2(idx=i, curr_sum=curr_sum + can, path=path, candidates=candidates, target=target, result=result)

            path.pop()

if __name__ == "__main__":
    s: Solution = Solution()

    candidates: List[int] = [2, 3, 6, 7]
    target: int = 7

    result: List[List[int]] = s.combinationSum(candidates, target)

    print(result)