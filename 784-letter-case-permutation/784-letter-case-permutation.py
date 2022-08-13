from collections import deque

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        q  = deque([])
        
        # first character
        if s[0].isalpha():
            q.append(s[0])
            q.append(self.convert(s[0]))
        else:
            q.append(s[0])
        
        ret = []
        while q:
            item = q.popleft()
            
            if len(item) == len(s):
                ret.append(item)
                continue
            
            next_i = len(item)
            
            if next_i <= len(s)-1:
                if s[next_i].isalpha():
                    q.append(item + s[next_i])
                    q.append(item + self.convert(s[next_i]))
                else:
                    q.append(item + s[next_i])
        return ret
    
    # capaital -> normal, normal -> capital
    def convert(self, string: str) -> str:
        if string in 'abcdefghijklmnopqrstuvwxyz':
            return string.upper()
        elif string in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return string.lower()
        
        