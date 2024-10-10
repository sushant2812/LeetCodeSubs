class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l,r):
            substr = s[l:r+1]
            return substr == substr[::-1]
        res = []
        path = []
        def dfs(idx):
            if idx>=len(s):
                res.append(path.copy())
                return
            for right in range(idx,len(s)):
                if isPalindrome(idx,right):
                    path.append(s[idx:right+1])
                    dfs(right+1)
                    path.pop()
        dfs(0)
        return res