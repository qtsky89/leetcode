class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        s = 'l e e t c o d e' wordDict = ['leet', 'code']
                     ^       ^
        '''

        q = deque([0])

        visited = set()
        while q:
            i = q.pop()
            visited.add(i)

            if i == len(s):
                return True
            elif i > len(s):
                continue
            
            for word in wordDict:
                if s[i:i+len(word)] == word and i+len(word) not in visited:
                    q.append(i+len(word))
        return False

        
        

        