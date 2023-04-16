class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        1  2  3  4  5
        6  7  8  9  10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25

        1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13

        right -> down -> left -> up -> right ...
        direction = 0 1 2 3
        '''

        # current = [i, j, direction]
        current = [0,0,0]
        ret = []
        m, n = len(matrix), len(matrix[0])

        visited = set()
        while len(ret) < m * n:
            i, j, direction = current
            visited.add((i,j))
            ret.append( matrix[i][j])

            if direction == 0:
                if j + 1 <= n -1 and (i, j+1) not in visited:
                    current = [i, j+1, direction]
                else:
                    current = [i+1, j, (direction+1) % 4]
            elif direction == 1:
                if i + 1 <= m -1  and (i+1, j) not in visited:
                    current = [i+1, j, direction]
                else:
                    current = [i, j-1, (direction+1) % 4]
            elif direction == 2:
                if j - 1 >= 0 and (i, j-1) not in visited:
                    current = [i, j-1, direction]
                else:
                    current = [i-1, j, (direction+1) % 4]
            else:
                if i-1 >= 0  and (i-1, j) not in visited:
                    current = [i-1, j, direction]
                else:
                    current = [i, j+1, (direction+1) % 4]
        return ret
            


