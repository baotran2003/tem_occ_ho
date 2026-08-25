import heapq
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    # while len(stones) > 1:
    #     stones.sort()
    #
    #     max_stone: int = stones.pop()
    #     max_second_stone: int = stones.pop()
    #
    #     dif: int = max_stone - max_second_stone
    #
    #     if dif > 0:
    #         stones.append(dif)
    #
    # return stones[0] if stones else 0

    # while len(stones) > 1:
    #     max_idx: int = 0
    #     max_second_idx: int = 0
    #
    #     for i in range(1, len(stones)):
    #         if stones[i] > stones[max_idx]:
    #             max_idx = i
    #     max_stone: int = stones.pop(max_idx)
    #
    #     for i in range (1, len(stones)):
    #         if stones[i] > stones[max_second_idx]:
    #             max_second_idx = i
    #     max_second_stone: int = stones.pop(max_second_idx)
    #
    #     if max_second_stone != max_stone:
    #         stones.append(max_stone - max_second_stone)
    # return stones[0] if stones else 0

    # max_heap:
    stones_negative: List[int] = [-x for x in stones]
    heapq.heapify(stones_negative)

    while len(stones_negative) > 1:
        max_stone: int = heapq.heappop(stones_negative)
        max_second_stone: int = heapq.heappop(stones_negative)

        if max_stone != max_second_stone:
            dif: int = max_stone - max_second_stone
            heapq.heappush(stones_negative, dif)

    return -stones_negative[0] if stones_negative else 0


if __name__ == "__main__":
    stones: List[int] = [1]
    print(lastStoneWeight(stones))