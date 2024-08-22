class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        ans=[]
        for i in range(len(nums)):
            other = target-nums[i]
            if other in hashmap:
                return [i, hashmap[other]]
            hashmap[nums[i]]=i