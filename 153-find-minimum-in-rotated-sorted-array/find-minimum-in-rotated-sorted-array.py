class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        ans = nums[0]
        r = len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                ans = min(ans,nums[l])
                return ans
            m = (l+r)//2
            ans = min(ans,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return ans