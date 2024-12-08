class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for idx,num in enumerate(nums):
            if idx>0 and nums[idx]==nums[idx-1]:
                continue
            left=idx+1
            right=len(nums)-1
            while left<right:
                ans=num+nums[left]+nums[right]
                if ans>0:
                    right-=1
                elif ans<0:
                    left+=1
                else:
                    res.add((num,nums[left],nums[right]))
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return list(res)