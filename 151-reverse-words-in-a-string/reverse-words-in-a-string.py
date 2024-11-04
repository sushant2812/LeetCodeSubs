class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        a = [i for i in l if i!='']
        a.reverse()
        print(a)
        return ' '.join(a)