class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ret = False

        visited = set()
        def dfs(remaining: str) -> None:
            if remaining in visited:
                return
            else:
                visited.add(remaining)

            if remaining == '':
                nonlocal ret
                ret = True
                return
            
            for word in wordDict:
                if word == remaining[:len(word)]:
                    dfs(remaining[len(word):])
        dfs(s)

        return ret
        