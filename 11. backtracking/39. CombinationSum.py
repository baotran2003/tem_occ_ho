from typing import List

# Thực tế: Giả sử bạn là máy ATM, bạn có các mệnh giá tiền [10k, 20k, 50k] (số lượng tờ tiền là vô hạn). Khách hàng muốn rút 100k (Target). Có bao nhiêu cách để máy ATM trả đúng số tiền đó?
# Chiều cao (độ sâu) của Call Stack lớn nhất=len(path). (Ví dụ path=[2,2,2,2] thì stack dài 5 tầng - tính cả tầng số 0).

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path: List[int] = []
        result: List[List[int]] = []

        curr_sum: int = 0

        self.backtracking(idx=0, curr_sum=curr_sum, path=path, candidates=candidates, target=target, result=result )

        return result

    def backtracking(self, idx: int, curr_sum: int, path: List[int], candidates: List[int], target: int, result: List[List[int]]) -> None:
        # Base Case: == target || > target
        if curr_sum > target:
            return
        if curr_sum == target:
            result.append(path[:])
            return

        for i in range(idx, len(candidates)):
            candidate: int = candidates[i]
            path.append(candidate)

            self.backtracking(idx=i, curr_sum=curr_sum+candidate, path=path, candidates=candidates,target=target,result=result)

            path.pop()


if __name__ == "__main__":
    s: Solution = Solution()

    candidates: List[int] = [2, 3, 5]
    target: int = 8

    result: List[List[int]] = s.combinationSum(candidates, target)

    print(result)
