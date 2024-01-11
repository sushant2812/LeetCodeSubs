class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=''.join(x for x in s if x.isalnum())
        final=final.lower()
        i=0
        j=len(final)-1
        while i<=j:
            if(final[i]==final[j]):
                i+=1
                j-=1
            else:
                print(final[i])
                print(final[j])
                return False
        return True