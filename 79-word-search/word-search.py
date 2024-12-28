class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ret = False
        def dfs(i: int, j: int, current_word: str, visited: set[tuple[int, int]]) -> None:
            current_word += board[i][j]
            visited.add((i, j))
            
            if current_word == word:
                nonlocal ret
                ret = True
                return
            
            if len(current_word) > len(word):
                return
            
            if (i+1) <= len(board)-1 and board[i+1][j] == word[len(current_word)] and (i+1, j) not in visited:
                dfs(i+1, j, current_word, set(visited))
            
            if (j+1) <= len(board[0])-1 and board[i][j+1] == word[len(current_word)] and (i, j+1) not in visited:
                dfs(i, j+1, current_word, set(visited))
            
            if (i-1) >= 0 and board[i-1][j] == word[len(current_word)] and (i-1, j) not in visited:
                dfs(i-1, j, current_word, set(visited))

            if (j-1) >= 0 and board[i][j-1] == word[len(current_word)] and (i, j-1) not in visited:
                dfs(i, j-1, current_word, set(visited))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, '', set())
        

        return ret