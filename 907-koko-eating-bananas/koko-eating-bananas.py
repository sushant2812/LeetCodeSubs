class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_speed(temp,piles):
            return sum(ceil(pile/temp)for pile in piles)
        left = 1 
        right = max(piles)
        res = max(piles)
        while left <= right:
            temp = (left+right)//2
            hrs = find_speed(temp,piles)
            if hrs<=h:
                res=min(res,temp)
                right=temp-1
            else:
                left=temp+1
        return res