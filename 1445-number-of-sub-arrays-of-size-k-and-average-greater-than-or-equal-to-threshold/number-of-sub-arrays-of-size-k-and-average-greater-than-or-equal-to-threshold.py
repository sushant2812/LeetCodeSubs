class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        window=[]
        temp =0
        for i in range(k):
            window.append(arr[i])
            temp += arr[i]
        if (temp/k)>=threshold:
            ans+=1
        for i in range(k,len(arr)):
            window.append(arr[i])
            temp-=window[0]
            temp+=arr[i]
            window.pop(0)
            if (temp/k)>=threshold:
                ans+=1
        return ans