from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ret = []
        q = deque([[s, []]])

        while q:
            remain, current_list = q.popleft()

            if remain == '':
                ret.append(' '.join(current_list))
                continue
            
            for word in wordDict:
                if remain[:len(word)] == word:
                    q.append([remain[len(word):], [*current_list, word]])
        
        return ret