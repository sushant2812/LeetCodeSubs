## Max Heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            temp_1 = -heapq.heappop(max_heap) 
            temp_2 = -heapq.heappop(max_heap) 
            if temp_1!=temp_2:
                heapq.heappush(max_heap,-(temp_1-temp_2))
            
        if not max_heap:
            return 0
        return -max_heap[0]