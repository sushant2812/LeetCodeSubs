class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = float('inf')
        temp_sum = 0
        for right in range(len(nums)):
            temp_sum += nums[right]
            while temp_sum>=target:
                ans = min(ans,right-left+1)
                temp_sum -= nums[left]
                left+=1
        if ans==float('inf'):
            return 0
        return ans