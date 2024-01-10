class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                temp = num+1
                while temp in nums:
                    temp+=1
                ans = max(ans, temp-num)
        return ans