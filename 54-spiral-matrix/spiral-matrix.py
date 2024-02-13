from collections import deque

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        1   2  3  4  5
        6   7  8  9 10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25
        

        1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13
        '''

        visited = set()

        #              right    down   left      up
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        q = deque([[0, 0, 0]])

        ret = []
        while q:
            i, j, k = q.popleft()
            visited.add((i, j))
            ret.append(matrix[i][j])

            if len(visited) == len(matrix) * len(matrix[0]):
                return ret

            next_i = i + directions[k][0]
            next_j = j + directions[k][1]

            if not(0 <= next_i <= len(matrix)-1) or not (0 <= next_j <= len(matrix[0])-1) or (next_i, next_j) in visited:
                k += 1
                k %= 4
            
            next_i = i + directions[k][0]
            next_j = j + directions[k][1]

            q.append([next_i, next_j, k])

            





        