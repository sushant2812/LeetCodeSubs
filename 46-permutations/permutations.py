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
                compare.add(nums[i])
                temp.append(nums[i])
                dfs(temp,compare)
                compare.remove(nums[i])
                temp.remove(nums[i])
        dfs([],set())
        return res