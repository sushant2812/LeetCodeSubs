class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        temp_length = 1
        set_of_nums = set(nums)
        for num in set_of_nums:
            if num-1 not in set_of_nums:
                temp = num+1
                temp_length=1
                while temp in set_of_nums:
                    temp_length+=1
                    temp+=1
                ans=max(temp_length,ans)
        return ans