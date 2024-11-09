class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l,r):
            substr = s[l:r+1]
            return substr==substr[::-1]
        res=[]
        temp=[]
        def dfs(idx):
            if idx>=len(s):
                res.append(temp.copy())
                return
            for right in range(idx,len(s)):
                if isPalindrome(idx,right):
                    temp.append(s[idx:right+1])
                    dfs(right+1)
                    temp.pop()
        dfs(0)
        return res