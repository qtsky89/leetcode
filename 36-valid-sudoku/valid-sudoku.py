class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in visited:
                    return False
                visited.add(board[i][j])
        
        # check all columns
        for j in range(9):
            visited = set()
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in visited:
                    return False
                visited.add(board[i][j])
        
        for i in range(3):
            for j in range(3):
                visited = set()
                for k in range(3):
                    for l in range(3):
                        if board[3*i+k][3*j+l] != '.' and board[3*i+k][3*j+l] in visited:
                            return False
                        visited.add(board[3*i+k][3*j+l])
        return True