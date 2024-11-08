class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]^nums[i]
        ans=[0]*len(nums)
        mask=(1<<maximumBit)-1 
        for i in range(len(nums)):
            curr = prefix[len(prefix) - 1 - i]
            ans[i] = curr ^ mask

        return ans
            
