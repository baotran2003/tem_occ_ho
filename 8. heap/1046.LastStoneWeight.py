import heapq
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    # brute force -> O(n x n)
    while len(stones) > 1:
        max_idx: int = 0
        for i in range (1, len(stones)):
            if stones[i] > stones[max_idx]:
                max_idx = i
        first_max: int = stones.pop(max_idx)

        second_idx: int = 0
        for i in range(1, len(stones)):
            if stones[i] > stones[second_idx]:
                second_idx = i
        second_max: int = stones.pop(second_idx)

        diff: int = first_max - second_max
        if diff > 0:
            stones.append(diff)

    if len(stones) >= 1:
        return stones[0]
    else:
        return 0

    #sort
    # while len(stones) > 1:
    #     stones.sort()
    #     largest: int = stones.pop()
    #     second_largest: int = stones.pop()
    #
    #     diff: int =  largest - second_largest
    #     if diff > 0:
    #         stones.append(diff)
    #
    # if len(stones) >= 1:
    #     return stones[0]
    # else:
    #     return 0

    # stones_negative: List[int] = [-x for x in stones]
    # heapq.heapify(stones_negative) # convert list -> heap   On
    #
    # print(stones_negative)
    #
    # while len(stones_negative) > 1:
    #     stone1: int = heapq.heappop(stones_negative)
    #     print(stones_negative)
    #     stone2: int = heapq.heappop(stones_negative)
    #
    #     if stone1 != stone2:
    #         heapq.heappush(stones_negative, stone1 - stone2)
    #
    # if len(stones_negative) >= 1:
    #     return -stones_negative[0]
    # else:
    #     return 0



if __name__ == "__main__":
    stones: List[int] = [1, 1, 2, 7, 4, 8]
    print(lastStoneWeight(stones))