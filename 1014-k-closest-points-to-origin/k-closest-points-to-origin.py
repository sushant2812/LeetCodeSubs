class Solution:
    def originDistance(self,x1,y1):
        return x1**2 + y1**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            temp = self.originDistance(point[0],point[1])
            heapq.heappush(distance,(temp,point))
        res = []
        for i in range(k):
            temp_distance, temp_point = heapq.heappop(distance)
            res.append(temp_point)
        return res