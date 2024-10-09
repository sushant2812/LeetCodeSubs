class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substr):
            return substr == substr[::-1]
        res = []
        def backtrack(start, path):
            if start==len(s):
                res.append(path.copy())
                return
            for end in range(start+1, len(s)+1):
                if isPalindrome(s[start:end]):
                    backtrack(end,path + [s[start:end]])
        backtrack(0,[])
        return res