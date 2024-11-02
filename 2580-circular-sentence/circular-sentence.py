class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0]!=sentence[-1]:
            return False
        chk = 0
        for i in range(len(sentence)):
            if sentence[i]!=' ':
                continue
            else:
                if sentence[i-1]!=sentence[i+1]:
                    return False

        return True