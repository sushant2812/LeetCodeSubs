import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t=collections.Counter(nums)
        a=t.most_common(k)
        ans = []
        for i in a:
            ans.append(i[0])
        return ans