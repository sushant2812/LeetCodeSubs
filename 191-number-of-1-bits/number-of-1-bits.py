class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n))
        a=Counter(n)
        return a['1']
        