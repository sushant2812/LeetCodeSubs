from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1_counter = [0] * 26
        s2_counter = [0] * 26
    
        for i in range(len(s1)):
            s1_counter[ord(s1[i]) - 97] += 1
            s2_counter[ord(s2[i]) - 97] += 1

        if s1_counter==s2_counter:
            return True
        window_size = len(s1)
        for i in range(window_size,len(s2)):
            print(s1_counter, s2_counter)
            s2_counter[ord(s2[i]) - 97] += 1
            s2_counter[ord(s2[i - window_size]) - 97] -= 1
            if s1_counter==s2_counter:
                return True
        return False