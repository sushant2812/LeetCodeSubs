class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=collections.Counter(s)
        b=collections.Counter(t)
        return a==b