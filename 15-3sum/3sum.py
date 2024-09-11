class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for index, num in enumerate(nums):
            left = index+1
            right = len(nums)-1
            while left < right:
                result = num+nums[left]+nums[right]
                if result==0:
                
                    res.add((num, nums[left],nums[right]))
                if result>0:
                    right-=1
                else:
                    left+=1
        return res
