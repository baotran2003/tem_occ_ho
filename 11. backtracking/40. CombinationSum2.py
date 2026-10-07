from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr_sum: int = 0
        path: List[List[int]] = []
        result: List[List[int]] = []

        self.backtracking(idx=0, curr_sum=curr_sum, path=path, candidates=candidates, target=target, result=result)

        return result

    def backtracking(self, idx: int, curr_sum: int, path: List[int], candidates: List[int], target: int,
                     result: List[List[int]]) -> None:

        # Base case: curr_sum == target || curr_sum > target
        if curr_sum == target:
            result.append(path[:])
            return

        for i in range(idx, 4):
            # Tỉa nhanh
            if curr_sum + candidates[i] > target:
                break

            # 2. Bỏ qua số trùng tại CÙNG một cấp độ vòng lặp (cùng độ sâu cây quyết định)
            if i > idx and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])

            self.backtracking(idx=i + 1, curr_sum=curr_sum + candidates[i], path=path, candidates=candidates,
                              target=target, result=result)

            path.pop()


if __name__ == "__main__":
    candidates: List[int] = [1, 1, 2, 5]  # 3
    target: int = 3

    s: Solution = Solution()
    result: List[List[int]] = s.combinationSum2(candidates, target)

    print(result)