from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a = defaultdict(int)
        for word in s1.split():
            a[word] +=1
        for word in s2.split():
            a[word] +=1
        ans = []
        for word in a:
            if a[word]==1:
                ans.append(word)
        return ans
        