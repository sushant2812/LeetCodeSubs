class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t=set(nums)
        t=list(t)
        return not(len(t)==len(nums))