import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp_0=collections.Counter(s1)
        s3=list(s2[:len(s1)])
        temp=collections.Counter(s3)
        if(temp==temp_0):
            return True
        for i in range(len(s1),len(s2)):
            s3.pop(0)
            s3.append(s2[i])
            temp=collections.Counter(s3)
            if(temp==temp_0):
                return True
            else:
                continue
        return False