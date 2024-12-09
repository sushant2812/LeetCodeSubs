class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0]*n for i in range(n)]
        k=1
        l=t=0
        r=b=n-1
        while l<=r and t<=b:
            for i in range(l,r+1):
                ans[t][i]=k
                k+=1
            t+=1
            for i in range(t,b+1):
                ans[i][r]=k
                k+=1
            r-=1
            if l>r or t>b:
                break
            for i in range(r,l-1,-1):
                ans[b][i]=k
                k+=1
            b-=1
            for i in range(b,t-1,-1):
                ans[i][l]=k
                k+=1
            l+=1
        return ans