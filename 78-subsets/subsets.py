class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet=[]
        subSet=[]
        def dfs(idx):
            powerSet.append(subSet.copy())
            for i in range(idx,len(nums)):
                subSet.append(nums[i])
                dfs(i+1)
                subSet.pop()
        dfs(0)
        return powerSet