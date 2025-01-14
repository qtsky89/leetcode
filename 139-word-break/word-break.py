class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ret = False

        visited = set()
        def dfs(i: int) -> None:
            if i == len(s):
                nonlocal ret
                ret = True
                return
            
            if ret:
                return

            visited.add(i)
            
            for word in wordDict:
                if s[i:i+len(word)] == word and i+len(word) not in visited:
                    dfs(i+len(word))
            
        dfs(0)

        return ret