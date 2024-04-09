class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        1 2 3
        4 5 6
        7 8 9

        op1                             (0 0)       (2 2)
        3 2 1    (0 0) (0 1) (0 2)      (0 1) < = > (1 2)
        6 5 4    (1 0) (1 1) (1 2)      (1 0) < = > (2 1)
        9 8 7    (2 0) (2 1) (2 2)

        op2
        7 4 1
        8 5 2 
        9 6 3


        1 2 3 4
        5 6 7 8
        9 10 11 12
        13 14 15 16

        
        1 5 9 13
        2 6 10 14
        3 7 11 15
        4 8 12 16

           13  9  5  1
           14  10  6  2
           15  11  7  3
           16  12  8  4

        00 01 02 03         02 -> 13
        10 11 12 13         01 -> 23
        20 21 22 23         00 -> 33
        30 31 32 33         11 -> 22
                            10 -> 32
                            20 -> 31


        """
        n = len(matrix)
        # op1
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # op2
        n = len(matrix)
        for i in range(n):
            j, k = 0, n-1
            mid = (j + k) // 2
            while j <= mid:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
        
        


        
        