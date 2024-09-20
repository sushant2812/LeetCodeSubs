class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length_word = len(s)
        string_reversed = s[::-1]
        for i in range(length_word):
            if s[:length_word-i]==string_reversed[i:]:
                return string_reversed[:i]+s
        return ""