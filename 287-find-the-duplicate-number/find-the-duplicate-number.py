import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=collections.Counter(nums)
        return a.most_common(1)[0][0]