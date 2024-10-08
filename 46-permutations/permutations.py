class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        superSet = []
        def dfs(current,compare):
            if len(current)==len(nums):
                superSet.append(current.copy())
                return
            for i in range(len(nums)):
                if nums[i] in compare:
                    continue
                else:
                    current.append(nums[i])
                    compare.add(nums[i])
                    dfs(current,compare)
                    current.pop()
                    compare.remove(nums[i])
        dfs([],set())
        return superSet