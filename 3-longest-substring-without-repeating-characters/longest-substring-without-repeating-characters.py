class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s = 'p    w    w    k    e   w'
visited[p]      p1 p2
        '''

        p1, p2 = 0 , 0

        visited = set()

        maximum_length = 0

        while p1 <= p2 <= len(s)-1:
            while s[p2] in visited:
                visited.remove(s[p1])
                p1 += 1
            visited.add(s[p2])
            maximum_length = max(maximum_length, p2 - p1 + 1)
            p2 += 1
        
        return maximum_length

