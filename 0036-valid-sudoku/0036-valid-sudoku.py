class Solution:
    def checkSmall(self, board: list[list[str]], i, j: int) -> bool:
        ret = set()
        
        for x in range(i, i+3):
            for y in range(j, j+3):
                if board[x][y] != '.' and board[x][y] in ret:
                    return False
                ret.add(board[x][y])
        return True
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        
        # row check
        for i in range(m):
            count_dot = board[i].count('.')
            
            if (m-count_dot) != len(set(board[i]) - {'.'}):
                return False
        
        # colmn check
        for j in range(n):
            tmp = []
            for i in range(m):
                tmp.append(board[i][j])
                
            count_dot = tmp.count('.')

            if (n-count_dot) != len(set(tmp) - {'.'}):
                return False
        
        # 3*3 check
        for i in range(3):
            for j in range(3):
                if self.checkSmall(board, i*3, j*3) is False:
                    return False
                
        return True
        
                
            