class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        b=[stone*-1 for stone in stones]
        heapq.heapify(b)
        while len(b)>1:
            stone1=heapq.heappop(b)*-1
            stone2=heapq.heappop(b)*-1
            if stone1==stone2:
                continue
            else:
                stone=abs(stone1-stone2)*-1
                heapq.heappush(b,stone)
        return abs(b[0]) if len(b)==1 else 0