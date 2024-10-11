class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key = lambda x: times[x][0])
        empty = list(range(len(times)))
        taken = []
        for i in order:
            ar, lv = times[i]
            while taken and taken[0][0] <= ar:
                heappush(empty,heappop(taken)[1])
            seat =heappop(empty)
            if i==targetFriend:
                return seat
            heappush(taken,(lv,seat))
    