
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix=[]
        prefix_sum=0
        for i in range(len(nums)):
            prefix.append(prefix_sum)
            prefix_sum+=nums[i]
        prefix.append(prefix_sum)
        dq = deque()  
        min_len = float('inf')
        
        for i in range(len(prefix)):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_len if min_len != float('inf') else -1

