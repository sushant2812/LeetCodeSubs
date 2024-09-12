class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for i in words:
            word = set(i)
            diff = word.difference(allowed)
            if diff!=set():
                continue
            ans+=1
        return ans