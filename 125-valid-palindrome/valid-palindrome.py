class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward=''.join(x for x in s if x.isalnum())
        forward=forward.lower()
        temp=list(forward)
        temp.reverse()
        reverse=''.join(x for x in temp)
        return forward==reverse