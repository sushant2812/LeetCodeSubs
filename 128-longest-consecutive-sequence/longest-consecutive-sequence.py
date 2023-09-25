class Solution(object):
    def longestConsecutive(self, nums):
        temp = set(nums)
        ans = 0
        while len(temp)>0:
            curr = next(i for i in temp)
            prev = curr-1
            while curr in temp:
                temp.discard(curr)
                curr+=1
            while prev in temp:
                temp.discard(prev)
                prev-=1
            ans=max(ans,curr-prev-1)
        return ans