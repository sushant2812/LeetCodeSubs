class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        pre = 1
        suf = 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-i-1] *= suf
            suf *= nums[-i-1]
        return ans