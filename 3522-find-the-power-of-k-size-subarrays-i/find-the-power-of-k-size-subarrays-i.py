class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cnt=1
        l=0
        res=[]
        for r in range(len(nums)):
            if r>0 and nums[r-1]+1==nums[r]:
                cnt+=1
            if r-l+1>k:
                if nums[l+1]==nums[l]+1:
                    cnt-=1
                l+=1
            if r-l+1==k:
                if cnt==k:
                    res.append(nums[r])
                else:
                    res.append(-1)
        return res