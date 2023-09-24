import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            temp = list(collections.Counter(i).elements())
            temp.sort()
            temp = ''.join(temp)
            if temp not in a:
                a[temp] = []
            a[temp].append(i)
        return a.values()