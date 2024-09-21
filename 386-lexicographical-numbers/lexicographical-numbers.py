class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num=[]
        curr = 1
        for i in range(1,n+1):
            num.append(curr)
            if(curr*10<=n):
                curr = curr*10
            else:
                while(curr%10 ==9 or curr>=n):
                    curr = curr//10
                curr+=1
        return num