class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s =   p  w  w  k  e  w
                    ^^
        
        visited = {}
        '''

        if len(s) == 0:
            return 0

        p1, p2 = 0, 0
        visited = set(s[p2])
        longest_length = 0

        while p1 <= p2 and p2 <= len(s)-1:
            longest_length = max(longest_length, p2-p1+1)

            p2 += 1
            if p2 <= len(s)-1:
                if s[p2] not in visited:
                    visited.add(s[p2])
                else:
                    while s[p1] != s[p2]:
                        visited.remove(s[p1])
                        p1+=1
                    p1+=1
        return longest_length

