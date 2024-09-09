class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            temp = list(i)
            temp.sort()
            temp = ''.join(temp)
            if temp not in ans:
                ans[temp] = []
            ans[temp].append(i)
        return ans.values()