from collections import Counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)
        def dfs(temp):
            if len(temp)==len(nums):
                res.append(temp.copy())
                return
            for num in nums:
                if counter[num]==0:
                    continue
                counter[num] -= 1
                dfs(temp+[num])
                counter[num] += 1
        dfs([])
        return res