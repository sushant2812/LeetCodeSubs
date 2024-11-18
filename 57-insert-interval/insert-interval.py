class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        merged=[]
        intervals.sort(key = lambda x: x[0])
        previous = intervals[0]
        for i in intervals[1:]:
            if i[0]<=previous[1]:
                previous[1] = max(previous[1],i[1])
            else:
                merged.append(previous)
                previous = i
        merged.append(previous)
        return merged