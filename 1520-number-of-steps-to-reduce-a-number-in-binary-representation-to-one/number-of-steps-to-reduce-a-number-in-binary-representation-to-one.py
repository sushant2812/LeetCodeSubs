class Solution:
    def numSteps(self, s: str) -> int:
        a = int(s,2)
        steps = 0
        while a!=1:
            if(a%2==0):
                steps+=1
                a=a//2
            else:
                a=a+1
                steps+=1
        return steps