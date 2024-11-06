class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        map = {}
        for point in points:
            if point[0] not in map:
                map[point[0]] = set()
            map[point[0]].add(point[1])
        for i in range(len(points)):
            for j in range(len(points)):
                x1,y1 = points[i][0], points[i][1]
                x2,y2 = points[j][0], points[j][1]
                if x1!=x2 and y1!=y2:
                    if (y2 in map[x1] and y1 in map[x2]):
                        min_area = min(min_area, abs(x1-x2)*abs(y1-y2))
        return min_area if min_area!=float('inf') else 0