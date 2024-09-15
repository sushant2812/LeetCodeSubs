class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        size, ans = 0, 0
        for num in nums:
            if num==target:
                size+=1
            else:
                size=0
            ans = max(ans,size)
        return ans