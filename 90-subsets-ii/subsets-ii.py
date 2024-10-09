class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        subSet = []
        nums.sort()
        def dfs(idx):
            if idx>=len(nums):
                powerSet.append(subSet.copy())
                return
            subSet.append(nums[idx])
            dfs(idx+1)
            subSet.pop()
            while idx+1<len(nums) and nums[idx]== nums[idx+1]:
                idx+=1
            dfs(idx+1)
        dfs(0)
        return powerSet