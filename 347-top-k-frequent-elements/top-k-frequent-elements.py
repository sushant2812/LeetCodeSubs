import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t=collections.Counter(nums)
        a=t.most_common(k)
        b=[]
        for i in a:
            b.append(i[0])
        return b