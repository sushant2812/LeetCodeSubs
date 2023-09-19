class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        pre=1
        suf=1
        for i in range(len(nums)):
            a[i]*=pre
            pre*=nums[i]
            a[-1-i]*=suf
            suf*=nums[-1-i]
        return a