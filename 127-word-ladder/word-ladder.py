from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l={}
        for i in wordList:
            l[i]=1
        q=deque()
        q.append((beginWord,1))
        while q:
            word=q[0][0]
            steps=q[0][1]
            if word in l:
                del l[word]
            q.popleft()
            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    zword=word[:i]+char+word[i+1:]
                    if zword in l:
                        q.append((zword,steps+1))
                    if zword==endWord and zword in l:
                        return steps+1
        return 0