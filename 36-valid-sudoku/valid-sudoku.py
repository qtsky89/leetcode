class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every row
        for i in range(len(board)):
            visited = set()

            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in visited:
                    return False
                visited.add(board[i][j])

        # check every column
        for j in range(len(board[0])):
            visited = set()

            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in visited:
                    return False
                visited.add(board[i][j])
        
        # check sub board
        for i in range(3):
            for j in range(3):
                visited = set()

                for k in range(3):
                    for l in range(3):
                        if board[3*i+k][3*j+l] == '.':
                            continue
                        
                        if board[3*i+k][3*j+l] in visited:
                            return False
                        visited.add(board[3*i+k][3*j+l])
        return True