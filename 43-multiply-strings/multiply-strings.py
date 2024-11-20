class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a=0
        b=0
        for i in num1:
            a=a*10+ord(i)-ord('0')
        for j in num2:
            b=b*10+ord(j)-ord('0')
        return str(a*b)
        