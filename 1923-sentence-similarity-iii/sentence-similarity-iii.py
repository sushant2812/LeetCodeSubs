class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words_1 = sentence1.split()
        words_2 = sentence2.split()

        if len(words_1)>len(words_2):
            words_1, words_2 = words_2, words_1
        
        i =0
        while i<len(words_1) and words_1[i] == words_2[i]:
            i+=1

        j = 0
        while j<len(words_1) and words_1[-(j+1)] == words_2[-(j+1)]:
            j+=1

        return i+j >= len(words_1)
