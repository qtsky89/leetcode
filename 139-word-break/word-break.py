class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        s = leetcode, worDict = ["leet", "code", "le", "xxx"]
            ^   
                ^   ^
              ^  
        '''

        q = [0]

        visited = set()
        while q:
            i = q.pop()
            
            if i == len(s):
                return True

            for word in wordDict:
                if s[i:i+len(word)] == word and (i+len(word)) not in visited:
                    visited.add(i)
                    q.append(i + len(word))
        
        return False