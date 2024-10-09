class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substr):
            return substr == substr[::-1]
        res = []
        def backtrack(idx,path):
            if idx>=len(s):
                res.append(path.copy())
                return
            for end in range(idx+1,len(s)+1):
                if isPalindrome(s[idx:end]):
                    backtrack(end,path+[s[idx:end]])
        backtrack(0,[])
        return res