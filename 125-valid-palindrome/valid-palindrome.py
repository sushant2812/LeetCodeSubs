class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''.join(x for x in s if x.isalnum())
        print(s)
        b=a.lower()
        c=list(b)
        c.reverse()
        c=''.join(x for x in c)
        return b==c
    
        