class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        s = " a  b   c"
             ij  ij  ij
        '''

        q = deque()

        for i in range(len(s)):
            q.append([i, i])

        for i in range(len(s)-1):
            # ex. aa, bb
            if s[i] == s[i+1]:
                q.append([i, i+1])
        
        count = 0
        while q:
            i, j = q.popleft()
            count += 1

            if i - 1 >= 0 and j + 1 <= len(s)-1 and s[i-1] == s[j+1]:
                q.append([i-1, j+1])

        return count
            
            