class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            temp = (left+right)//2
            hrs = sum(math.ceil(pile / temp) for pile in piles)
            if hrs<=h:
                res=min(res,temp)
                right= temp-1
            else:
                left = temp+1
        return res