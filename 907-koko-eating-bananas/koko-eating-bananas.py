class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        ans = right
        while left<=right:
            temp = (left+right) //2
            hrs = 0
            for i in piles:
                hrs+=math.ceil(i/temp)
            if hrs<=h:
                ans = min(ans,temp)
                right=temp-1
            else:
                left=temp+1
        return ans