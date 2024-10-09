from collections import Counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)
        def backtrack(subArray):
            if len(nums)==len(subArray):
                res.append(subArray.copy())
                return
            for num in nums:
                if counter[num]==0:
                    continue
                counter[num]-=1
                backtrack(subArray + [num])
                counter[num]+=1
                
        backtrack([])
        return res