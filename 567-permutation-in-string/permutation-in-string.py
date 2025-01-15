class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        s1 = abc
        {
            a : 1
            b : 1
            c : 1
        }

        s2 = e i d b a c o o o
             l   r
        {
            e : 1
            i : 1
            d : 1
        }
        '''

        c1 = Counter(s1)
        
        c2 = Counter(s2[:len(s1)])

        l, r = 0, len(s1)-1

        while r <= len(s2)-1:
            if c1 == c2:
                return True

            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                del c2[s2[l]]
            l, r = l+1, r+1

            if r <= len(s2)-1:
                if s2[r] in c2:
                    c2[s2[r]] += 1
                else:
                    c2[s2[r]] = 1

        return False
        