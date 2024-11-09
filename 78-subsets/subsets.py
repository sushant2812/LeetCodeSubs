class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset=[]
        subset=[]
        def dfs(idx):
            print(subset)
            powerset.append(subset.copy())
            for i in range(idx,len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return powerset