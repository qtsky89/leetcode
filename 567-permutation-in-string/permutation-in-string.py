class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)

        i, j = 0, len(s1)-1

        '''
        s2 = e i d b a o o o
             i j

        '''

        while j <= len(s2)-1:
            c2 = Counter(s2[i:j+1])            

            if c1 == c2:
                return True
            
            i, j = i+1, j+1

        return False

            

