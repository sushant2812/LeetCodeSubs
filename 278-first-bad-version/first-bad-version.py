# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        ans = n
        while left<=right:
            temp = (left+right)//2
            if isBadVersion(temp):
                ans = min(ans,temp)
                right=temp-1
            else:
                left=temp+1
        return ans