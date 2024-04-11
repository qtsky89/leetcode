class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        00->01->02->03
                     v
        10  11  12  13
                     v
        20  21  22  23
                     v
        30 < 31 < 32 < 33 

        right
        down
        left
        up
        '''

        #                  R       D       L        U
        direction_array = [(0, 1), (1, 0), (0, -1), (-1, 0)]


        ret = []
        visited = set()

        def dfs(i: int, j: int, direction_index: int) -> None:
            visited.add((i, j))
            ret.append(matrix[i][j])

            if len(visited) == len(matrix) * len(matrix[0]):
                return

            next_i = i + direction_array[direction_index][0]
            next_j = j + direction_array[direction_index][1]

            if (next_i, next_j) in visited or not(0 <= next_i <= len(matrix)-1) or not(0 <= next_j <= len(matrix[0])-1):
                direction_index = (direction_index+1) % 4
                next_i = i + direction_array[direction_index][0]
                next_j = j + direction_array[direction_index][1]

            if (next_i, next_j) not in visited:
                dfs(next_i, next_j, direction_index)
            
        dfs(0, 0, 0)

        return ret
        
