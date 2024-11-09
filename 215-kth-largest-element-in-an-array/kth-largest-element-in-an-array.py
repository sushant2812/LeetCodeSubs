class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        b = []
        a = [heapq.heappush(b,-num) for num in nums]
        ans=0
        for i in range(k):
            ans=heapq.heappop(b)*-1
        return ans