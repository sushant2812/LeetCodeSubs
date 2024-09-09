class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans =  defaultdict(list)
        for i in strs:
            temp = ''.join(sorted(i))
            ans[temp].append(i)
        return ans.values()