class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] in visited:
                    return False
                elif board[i][j] != '.':
                    visited.add(board[i][j])
        
        # colum check
        for j in range(9):
            visited = set()
            for i in range(9):
                if board[i][j] in visited:
                    return False
                elif board[i][j] != '.':
                    visited.add(board[i][j])
        
        # sub cell check
        hash_map = { (i, j) : set() for j in range(3) for i in range(3)}

        for i in range(9):
            for j in range(9):
                x = i // 3
                y = j // 3

                visited = hash_map[(x, y)]

                if board[i][j] in visited:
                    return False
                elif board[i][j] != '.':
                    visited.add(board[i][j])
        return True
        
        

        