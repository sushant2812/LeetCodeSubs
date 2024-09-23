class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        maxlength =0
        left =0
        count = {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            maxlength = max(maxlength, count[s[right]])
            if(right-left+1)-maxlength>k:
                count[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans