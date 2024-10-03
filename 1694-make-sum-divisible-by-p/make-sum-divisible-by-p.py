class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        temp_sum = sum(nums)
        remainder = temp_sum%p
        if remainder==0:
            return 0
        prefix_sum = 0 
        min_len = len(nums)
        remainder_map = {0:-1}
        for i,num in enumerate(nums):
            prefix_sum = (prefix_sum+num)%p
            required = (prefix_sum - remainder)%p
            if required in remainder_map:
                min_len = min(min_len,i-remainder_map[required])
            remainder_map[prefix_sum] = i
        return min_len if min_len < len(nums) else -1