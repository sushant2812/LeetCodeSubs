class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(temp,compare):
            if len(temp)==len(nums):
                res.append(temp.copy())
                return
            for i in range(len(nums)):
                if nums[i] in compare:
                    continue
                else:
                    temp.append(nums[i])
                    compare.add(nums[i])
                    dfs(temp,compare)
                    temp.remove(nums[i])
                    compare.remove(nums[i])
        dfs([],set())
        return res