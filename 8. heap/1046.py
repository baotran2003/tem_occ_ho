from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:

            # Khởi tạo từ 2 phần tử đầu
            if stones[0] >= stones[1]:
                max_stone = stones[0]
                max_se_stone = stones[1]
                idx = 0
                idx_second_max = 1
            else:
                max_stone = stones[1]
                max_se_stone = stones[0]
                idx = 1
                idx_second_max = 0

            # Tìm viên lớn nhất và lớn nhì
            for i in range(2, len(stones)):
                if stones[i] > max_stone:
                    max_se_stone = max_stone
                    idx_second_max = idx

                    max_stone = stones[i]
                    idx = i

                elif stones[i] > max_se_stone:
                    max_se_stone = stones[i]
                    idx_second_max = i

            if max_stone != max_se_stone:
                stones[idx] = max_stone - max_se_stone
                stones.pop(idx_second_max)

            else:
                # Pop index lớn trước để không bị lệch
                if idx > idx_second_max:
                    stones.pop(idx)
                    stones.pop(idx_second_max)
                else:
                    stones.pop(idx_second_max)
                    stones.pop(idx)

        return stones[0] if stones else 0

if __name__ == "__main__":
    # stones = [2, 7, 4, 1, 8, 1]
    stones = [8, 8, 4, 7, 1]

    print(Solution().lastStoneWeight(stones))