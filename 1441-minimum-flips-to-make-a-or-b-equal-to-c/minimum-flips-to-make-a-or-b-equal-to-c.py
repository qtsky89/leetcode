class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        '''
        OR
        X  Y  X OR Y
        0  0     0
        0  1     1
        1  0     1
        1  1     1

        ex.1

        a = 2, b = 6, c = 6

        0 0 1V 0
        0 1 1V 0V 
        
        0 1 0  1

        
        1 0 0 0
        0 0 1 1
        0 1 0 1

        1 1 0 1 => 3

        '''

        total_flip = 0
        while a > 0 or b > 0 or c > 0:
            x = a&1
            y = b&1
            z = c&1

            # no need to flip
            if (x | y) == z:
                a, b, c = a >> 1, b >> 1, c >> 1
                continue
            elif x == 1 and y == 1 and z == 0:
                total_flip += 2
            else:
                total_flip += 1
        
            a, b, c = a >> 1, b >> 1, c >> 1
        return total_flip
            
            
        