class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        freq={}
        subarr=deque()
        invalid=0
        temp_sum=0
        for i in range(k):
            subarr.append(nums[i])
            temp_sum+=nums[i]
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        if len(freq)==k:
            ans=max(ans,temp_sum)

        for i in range(k,len(nums)):
            a=subarr.popleft()
            temp_sum-=a
            freq[a]-=1
            if freq[a]==0:
                del freq[a]
            subarr.append(nums[i])
            temp_sum+=nums[i]
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
            if len(freq)==k:
                ans=max(ans,temp_sum)
        return ans