class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num=[]
        for i in range(n):
            num.append(str(i+1))
        num.sort()
        return [int(i) for i in num]