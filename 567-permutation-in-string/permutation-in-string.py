class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        p1, p2 = 0, len(s1)-1

        s2_counter = Counter(s2[0:len(s1)])
        while p2 <= len(s2)-1:
            # compare value of counter
            if s1_counter == s2_counter:
                return True
            
            if p2+1 <= len(s2)-1:
                s2_counter[s2[p2+1]] += 1
            s2_counter[s2[p1]] -= 1

            p1, p2 = p1+1, p2+1
        return False