class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        # colum check
        for j in range(len(board[0])):
            s = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue  
                elif board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

        # 3*3 check
        for i in range(3):
            for j in range(3):
                s = set()
                
                for k in range(3):
                    for l in range(3):
                        if board[i*3 + k][j*3 + l] == '.':
                            continue
                        elif board[i*3 + k][j*3 + l] in s:
                            return False
                        else:
                            s.add(board[i*3 + k][j*3 + l])
        return True
        