class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        '''
        l : 1
        e : 2
        t : 1
        c : 1
        o : 1
        d : 1
        e : 1
        '''

        for index, char in enumerate(s):
            if c[char] == 1:
                return index
        return -1