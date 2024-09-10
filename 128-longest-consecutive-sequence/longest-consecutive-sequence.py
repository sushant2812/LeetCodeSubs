class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        set_of_nums = set(nums)
        for num in set_of_nums:
            if num-1 not in set_of_nums:
                temp = num+1
                while temp in set_of_nums:
                    temp +=1
                ans = max(temp-num,ans)
        return ans