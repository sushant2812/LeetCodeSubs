class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in ans:
                ans[temp]=[]
            ans[temp].append(i)
        return list(ans.values())