class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        s = "anagram" t = "nagaram"

        
        '''

        return Counter(s) == Counter(t)