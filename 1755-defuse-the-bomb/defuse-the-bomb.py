class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        ans=[0]*len(code)
        for i in range(len(code)):
            temp=0
            if k>0:
                for j in range(i+1,i+k+1):
                    ans[i]+=code[j%len(code)]
            else:
                for j in range(i-abs(k),i):
                    ans[i]+=code[(j + len(code)) % len(code)]
        return ans