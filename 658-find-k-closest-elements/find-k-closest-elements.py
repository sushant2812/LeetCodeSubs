class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Create a min-heap
        heap = []
        
        for point in arr:
            dist = abs(x - point)
            # Push (distance, element) tuple into the heap
            heapq.heappush(heap, (dist, point))
        
        # Now pop the first k elements from the heap and collect the values
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        # Return the result sorted in ascending order of the elements
        return sorted(ans)