from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashmap = [0] * len(nums)
        def backtrack(subArray,hashmap):
            if len(nums)==len(subArray):
                
                if subArray.copy() not in res:
                    res.append(subArray.copy())
                    return
            for i in range(len(nums)):
                if hashmap[i]==1:
                    continue
                hashmap[i] = 1
                subArray.append(nums[i])
                backtrack(subArray,hashmap)
                subArray.pop()
                hashmap[i] = 0
        backtrack([],hashmap)
        return res