class Solution:


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2+point[1]**2
        ans=[]
        heap=[]
        for point in points:
            dist = distance(point)
            heapq.heappush(heap,(dist,point))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans