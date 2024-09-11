class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for index, num in enumerate(nums):
            if index>0 and nums[index]==nums[index-1]: ##Skippin duplicate of num1
                continue
            left = index+1
            right = len(nums)-1
            while left < right:
                result = num+nums[left]+nums[right]
                if result==0:
                    res.add((num, nums[left],nums[right]))
                    left=left+1
                    right=right-1
                    while left<right and nums[left]==nums[left-1]: ##Skippin duplicate of num2
                        left+=1
                elif result>0:
                    right-=1
                elif result<0:
                    left+=1
        return res
