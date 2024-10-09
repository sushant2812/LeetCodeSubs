from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)
        def backtrack(subArray):
            if len(nums)==len(subArray):
                res.append(subArray.copy())
                return
            for key in counter.keys():
                if counter[key]==0:
                    continue
                counter[key]-=1
                backtrack(subArray + [key])
                counter[key]+=1
                
        backtrack([])
        return res