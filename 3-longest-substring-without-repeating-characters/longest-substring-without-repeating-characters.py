class Solution:
    def lengthOfLongestSubstring(self, strings: str) -> int:
        '''
         a  b  c  a  b  c  b  b
                        ^     ^
        '''

        ret = 0

        p1, p2 = 0, 0
        visited = set()
        while p2 <= len(strings)-1:
            while strings[p2] in visited:
                visited.remove(strings[p1])
                p1 += 1

            visited.add(strings[p2])    
            ret = max(ret, p2-p1+1)

            p2 += 1
        
        return ret