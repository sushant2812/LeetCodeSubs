class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l=0
        res=[]
        cnt=1
        for r in range(len(nums)):
            if r>0:
                if nums[r-1]+1==nums[r]:
                    cnt+=1
            if r+1-l>k:
                if nums[l]+1==nums[l+1]:
                    cnt-=1
                l+=1
            if r+1-l==k:
                if cnt==k:
                    res.append(nums[r])
                else:
                    res.append(-1)
        return res
