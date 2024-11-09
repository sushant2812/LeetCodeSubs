class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerset=[]
        subset=[]
        nums.sort()
        def dfs(idx):
            if idx>=len(nums):
                print(subset)
                powerset.append(subset.copy())
                return
            subset.append(nums[idx])
            dfs(idx+1)
            subset.pop()
            while idx+1<len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            dfs(idx+1)
        dfs(0)
        return powerset