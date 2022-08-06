class Solution:
    # s1 = 'ab', s2 = 'eidbaooo'
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1, p2 = 0, len(s1)-1
        
        s1 = ''.join(sorted(s1))
        c1 = Counter(s1)
        
        while p2 <= len(s2)-1:
            if c1 == Counter(s2[p1:p2+1]):
                return True
            p1, p2 = p1+1, p2+1
        return False
            
            
        