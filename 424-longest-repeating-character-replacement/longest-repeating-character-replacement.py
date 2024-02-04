class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        c = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            c[s[r]] = 1 + c.get(s[r], 0)
            maxf =  max(c[s[r]], maxf)
            while (r-l+1)-maxf>k:
                c[s[l]]-=1
                l +=1
            ans = max(ans, r-l+1)
        return ans