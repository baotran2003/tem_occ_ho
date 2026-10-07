from typing import List

class Solution:
    def combination(self, candidates: List[int], k: int) -> List[List[int]]:
        path: List[int] = []
        result: List[List[int]] = []
        n: int = len(candidates)

        # idx: Vị trí bắt đầu duyệt trong mảng candidates (tránh lặp).
        self.backtracking(idx=0, n=n, candidates=candidates, k=k, path=path, result=result)

        return result

    def backtracking(self, idx: int, n:int, candidates: List[int], k: int, path: List[int], result: List[List[int]]) -> None:

        # Base case
        if len(path) == k:
            result.append(path[:])
            return

        for i in range (idx, n):
            path.append(candidates[i])
            self.backtracking(idx=i+1, n=n, candidates=candidates, k=k, path=path, result=result)

            path.pop()

            # python ngam tu dong: return None


if __name__ == "__main__":
    candidates: List[int] = [1, 2, 3, 4]
    k: int = 2
    s: Solution = Solution()
    result = s.combination(candidates, k)
    print(result)