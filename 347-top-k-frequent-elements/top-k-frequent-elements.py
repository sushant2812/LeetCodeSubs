class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        temp = collections.Counter(nums)
        a = temp.most_common(k)
        for i in a:
            ans.append(i[0])
        return ans