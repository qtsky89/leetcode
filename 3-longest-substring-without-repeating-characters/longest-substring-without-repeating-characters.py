class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s =  p w w k e w 
                 ^^                     p w

        '''

        p1, p2 = 0, 0
        visited = set()

        longest_length = 0
        while p2 <= len(s)-1:
            if s[p2] not in visited:
                longest_length = max(longest_length, p2-p1+1)
            else:
                while p1 <= p2 and (s[p2] in visited):
                    visited.remove(s[p1])
                    p1 += 1
            visited.add(s[p2])
            p2 += 1
        
        return longest_length