class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ''.join(x for x in s if x.isalnum())
        final_string = final_string.lower()
        left = 0
        right = len(final_string)-1
        while left<=right:
            if(final_string[left]==final_string[right]):
                left+=1
                right-=1
            else:
                return False
        return True