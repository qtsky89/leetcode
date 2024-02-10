from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        s = anagram
            {
                a: 3
                n: 1
            }

        t = nagaram
        '''

        return Counter(s) == Counter(t)


