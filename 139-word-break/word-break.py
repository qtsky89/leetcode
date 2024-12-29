class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        s = c a t s a n d o g           wordDict = cats, dog, sand, and, cat 
            ^
        '''

        ret = False
        visited = set()

        def dfs(current_index: index) -> None:
            nonlocal ret
            if ret:
                return

            if current_index == len(s):
                ret = True
                return
            
            visited.add(current_index)
            
            for word in wordDict:
                if s[current_index:current_index+len(word)] == word and current_index+len(word) not in visited:
                    dfs(current_index+len(word))
        
        dfs(0)

        return ret

        