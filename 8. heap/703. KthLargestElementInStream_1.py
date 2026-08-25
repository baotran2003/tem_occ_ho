import heapq
from typing import List
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    output = []

    kthLargest = KthLargest(3, [8, 5, 4, 2])
    output.append(None)

    output.append(kthLargest.add(3))
    output.append(kthLargest.add(5))
    output.append(kthLargest.add(10))
    output.append(kthLargest.add(9))
    output.append(kthLargest.add(4))

    print(output)
