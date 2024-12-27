class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)

        i, j = 0, len(s1)-1

        '''
        s2 = e i d b a o o o
             i j

        '''
        c2 = Counter(s2[i:j+1])
        while j <= len(s2)-1:
            if c1 == c2:
                return True

            if j+1 <= len(s2)-1:
                c2[s2[j+1]] += 1
                c2[s2[i]] -= 1

                if c2[s2[i]] == 0:
                    del c2[s2[i]]

            i, j = i+1, j+1

        return False

            

