class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)-1

        s1_counter = {}
        for s in s1:
            if s in s1_counter:
                s1_counter[s] += 1
            else:
                s1_counter[s] = 1

        s2_counter = {}
        for s in s2[:len(s1)]:
            if s in s2_counter:
                s2_counter[s] += 1
            else:
                s2_counter[s] = 1

        while j <= len(s2)-1:
            if s1_counter == s2_counter:
                return True
            
            if j+1 <= len(s2)-1:
                if s2[j+1] in s2_counter:
                    s2_counter[s2[j+1]] += 1
                else:
                    s2_counter[s2[j+1]] = 1
            
                s2_counter[s2[i]] -= 1
                if s2_counter[s2[i]] == 0:
                    del s2_counter[s2[i]]

            i, j = i+1, j+1
        

        return False