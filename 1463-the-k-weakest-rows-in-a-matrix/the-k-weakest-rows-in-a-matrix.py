class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        c={}
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count+=1
            c[i]=count
        sorted_soldiers = sorted(c.items(), key=lambda x:x[1])
        ans=[]
        for i in range(k):
            ans.append(sorted_soldiers[i][0])
        return ans