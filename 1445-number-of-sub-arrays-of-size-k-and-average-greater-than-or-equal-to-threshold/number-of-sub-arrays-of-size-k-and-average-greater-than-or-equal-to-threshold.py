class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        temp =0

        for i in range(k):
            temp+=arr[i]

        if temp/k>=threshold:
            ans+=1
        
        for i in range(k,len(arr)):
            temp+=arr[i]-arr[i-k]
            if temp/k>=threshold:
                ans+=1
        return ans