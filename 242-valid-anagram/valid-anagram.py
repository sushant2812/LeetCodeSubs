class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_Counter=collections.Counter(s)
        T_Counter=collections.Counter(t)
        return S_Counter==T_Counter