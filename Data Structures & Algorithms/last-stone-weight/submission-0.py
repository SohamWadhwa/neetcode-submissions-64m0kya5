import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            heapq.heappush(minHeap, -stone)

        while len(minHeap) > 1:
            x = -heapq.heappop(minHeap)
            y = -heapq.heappop(minHeap)

            if abs(y - x) != 0:
                heapq.heappush(minHeap, -abs(y - x))
        
        return -minHeap[0] if minHeap else 0
             