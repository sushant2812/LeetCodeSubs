class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans =  defaultdict(list)
        for i in strs:
            temp = list(i)
            temp.sort()
            temp = ''.join(temp)
            ans[temp].append(i)
        return ans.values()