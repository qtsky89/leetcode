class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        '''
        1. first make black list
        2. for nested loop, turn O -> X avoiding blacklist
        '''

        # 1. first make black list
        black_list: set[tuple[int, int]] = set()
        def dfs(i : int, j : int) -> None:
            black_list.add((i, j))

            if i+1 <= len(board)-1 and board[i+1][j] == 'O' and (i+1, j) not in black_list:
                dfs(i+1, j)
            
            if i-1 >= 0 and board[i-1][j] == 'O' and (i-1, j) not in black_list:
                dfs(i-1, j)
            
            if j+1 <= len(board[0])-1 and board[i][j+1] == 'O' and (i, j+1) not in black_list:
                dfs(i, j+1)
            
            if j-1 >= 0 and board[i][j-1] == 'O' and (i, j-1) not in black_list:
                dfs(i, j-1)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in black_list:
                    board[i][j] = 'X'
        