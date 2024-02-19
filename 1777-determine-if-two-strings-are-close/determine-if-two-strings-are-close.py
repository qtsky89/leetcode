class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Input: word1 = "b c a", word2 = "b c a"
        Output: true

        Input: word1 = "a", word2 = "aa"
        Output: false

        Input: word1 = "c a b b b a", word2 = "a b b c c c"
        word1 = {  
            a : 2
            b : 3
            c : 1
        }
        word2 = {
            a: 1
            b: 2
            c: 3
        }

        Output: true

        '''

        word1_hashmap = Counter(word1)
        word2_hashmap = Counter(word2)

        return sorted(word1_hashmap.keys()) == sorted(word2_hashmap.keys())    and sorted(word1_hashmap.values()) == sorted(word2_hashmap.values())