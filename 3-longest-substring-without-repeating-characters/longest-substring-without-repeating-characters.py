class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s =  a b c a b c b b
            ^^                   ret = 0

        '''

        longest_length = 0
        i, j = 0, 0
        visited = set()

        '''
        visited = {}
        '''
        while j <= len(s)-1:
            # need to make sure there is no repeating character
            while s[j] in visited:
                visited.remove(s[i])
                i += 1
            
            visited.add(s[j])

            longest_length = max(longest_length, j-i+1)

            j += 1
        
        return longest_length