class Solution:
    def firstUniqChar(self, strings: str) -> int:
        c = Counter(strings)

        '''
        l : 1
        e : 3
        t : 1
        c : 1
        o : 1
        d : 1
        '''

        for i, s in enumerate(strings):
            if c[s] == 1:
                return i
        return -1