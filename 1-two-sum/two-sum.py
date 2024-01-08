class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in ans:
                return [i,ans[rem]]
            ans[nums[i]]=i