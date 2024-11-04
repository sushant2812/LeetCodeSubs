class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        chk=0
        digit=1
        res=0
        index =0
        sign = 1
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        while index<len(s) and s[index].isdigit():
            digit=ord(s[index])-ord('0')
            if res > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            res=res*10+digit
            index+=1
        return res*sign