from typing import List
from collections import deque

class RecentCounter:

    # def __init__(self):
    #     self.calls: List[int] = []
    #
    # def ping(self, t: int) -> int:
    #     count: int = 0
    #
    #     self.calls.append(t)
    #
    #     for i in range (len(self.calls) -1, -1, -1):
    #         if self.calls[i] >= t - 3000:
    #             count += 1
    #         else:
    #             break
    #
    #     return count

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while len(self.queue) and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)

if __name__ == "__main__":
    recentCounter: RecentCounter  = RecentCounter();
    recentCounter.ping(1)
    recentCounter.ping(100)
    recentCounter.ping(3001)
    print(recentCounter.ping(8000))