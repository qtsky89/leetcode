from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        word1 = c a b b b a      a:2 b:3 c: 1 , 1, 2, 3
        word2 = a b b c c c      a:1 b:2 c: 3 , 1, 2, 3
        '''

        if len(word1) != len(word2):
            return False

        w1 = Counter(word1)
        w2 = Counter(word2)

        condition1 = sorted(w1.values()) == sorted(w2.values())
        condition2 = sorted(w1.keys()) == sorted(w2.keys())

        return condition1 and condition2
