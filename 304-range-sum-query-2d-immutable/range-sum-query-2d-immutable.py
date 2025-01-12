'''

    3  0  1  4  2                  3   0   4   8  10
    5  6  3  2  1                  8  14  21  31  43
    1  2  0  1  5
    4  1  0  1  7
    1  0  3  0  5

'''



class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        

        for i in range(len(self.prefix)):
            for j in range(len(self.prefix[0])):
                self.prefix[i][j] = (self.prefix[i-1][j] if i-1 >= 0 else 0) + (self.prefix[i][j-1] if j-1 >= 0 else 0) + matrix[i][j] - (self.prefix[i-1][j-1] if i-1 >= 0  and j-1 >= 0 else 0)
        
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2][col2] - (self.prefix[row1-1][col2] if row1-1 >= 0 else 0) - (self.prefix[row2][col1-1] if col1 -1 >= 0 else 0) + (self.prefix[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)