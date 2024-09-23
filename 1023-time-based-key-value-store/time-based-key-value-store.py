class TimeMap:

    def __init__(self):
        self.TimeMap ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.TimeMap.get(key,[])
        res = ""
        if values==[]:
            return res
        left = 0
        right =len(values)-1
        while left<=right:
            mid = (left+right)//2
            if values[mid][1]<=timestamp:
                res = values[mid][0]
                left = mid+1
            else:
                right = mid-1
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)