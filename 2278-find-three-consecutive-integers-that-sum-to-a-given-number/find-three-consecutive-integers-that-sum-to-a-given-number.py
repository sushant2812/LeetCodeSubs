class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3==0:
            num1 = num//3
            return [num1-1,num1,num1+1]
        return []