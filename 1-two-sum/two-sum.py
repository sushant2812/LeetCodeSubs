class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            ans = target-nums[i]
            if ans in hashmap:
                return [i,hashmap[ans]]
            hashmap[nums[i]]=i