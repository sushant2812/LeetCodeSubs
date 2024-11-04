class Solution:
    def compressedString(self, word: str) -> str:
        if len(word)==1:
            return "1"+word[0]
        l=0
        cnt=1
        res=[]
        for r in range(1,len(word)):
            if word[l]==word[r] and cnt<9:
                cnt+=1
            else:
                res.append(str(cnt)) 
                res.append(word[l])
                l=r
                cnt = 1
        res.append(str(cnt))
        res.append(word[r])
        return ''.join(res)