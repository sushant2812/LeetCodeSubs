from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        length_s1 = len(s1)
        counter2 = Counter(s2[:length_s1-1])
        left = 0
        for right in range(length_s1-1,len(s2)):
            counter2[s2[right]]+=1
            if counter2==counter1:
                return True
            counter2[s2[left]]-=1
            print(counter2)
            if counter2[s2[left]]==0:
                del counter2[s2[left]]
            left+=1
        return False