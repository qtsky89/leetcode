class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s = a   b    c    a    b    c    b    b 
            i,j

        '''
        if not s:
            return 0

        i, j = 0, 0
        visited = set()

        max_length = 0
        while i <= j <= len(s)-1:
            while s[j] in visited:
                visited.remove(s[i])
                i += 1
            
            visited.add(s[j])

            max_length = max(max_length, j-i + 1)

            j += 1
        return max_length
            


        return max_length