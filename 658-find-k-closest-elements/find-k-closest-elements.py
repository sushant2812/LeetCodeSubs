class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def distance(x,a):
            return abs(x-a)
        heap=[]
        for point in arr:
            dist=distance(x,point)
            heapq.heappush(heap,(dist,point))
        ans=[]
        for i in range(k):
            point = heapq.heappop(heap)
            ans.append(point[1])
        ans.sort()
        return ans