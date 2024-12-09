from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=Counter(p)
        c=[]
        len_substr= len(p)
        dic = Counter(s[:len_substr - 1])

        for i in range(len_substr-1,len(s)):
            dic[s[i]] += 1
            if dic == a:
                c.append(i - len_substr + 1)       
            # remove this char and add new char
            dic[s[i-len_substr+1]] -= 1
        return c