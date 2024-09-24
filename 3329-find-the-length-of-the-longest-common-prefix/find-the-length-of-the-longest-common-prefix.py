class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes_to_look = set()
        res = 0
        for val in arr1:
            while val not in prefixes_to_look and val>0:
                prefixes_to_look.add(val)
                val //=10
        for val in arr2:
            while val not in prefixes_to_look and val>0:
                val//=10
            if val>0:
                res= max(res,len(str(val)))
        return res