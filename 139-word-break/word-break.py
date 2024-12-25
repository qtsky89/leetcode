class Solution:
    '''
    s = "leetcode"
                  ^

    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ret = False
        visited = set()
        def dfs(current_i: int) -> None:
            nonlocal ret
            if ret:
                return

            if current_i == len(s):
                ret = True
                return
            
            visited.add(current_i)
            
            # word = leet
            for word in wordDict:
                if s[current_i:current_i+len(word)] == word and current_i+len(word) not in visited:
                    dfs(current_i+len(word))

        dfs(0)

        return ret