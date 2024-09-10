import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        length=len(nums)
        prefix = 1
        suffix = 1
        for i in range(length):
            ans.append(prefix)
            prefix=prefix*nums[i]
        for i in range(length-1,-1,-1):
            ans[i] = ans[i]*suffix
            suffix = suffix*nums[i]
        return ans