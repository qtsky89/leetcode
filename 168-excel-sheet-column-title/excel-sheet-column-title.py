class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        1 => A
        2 => B
        3 => C
        26 => Z
        27 => AA
        28 => AB
        52 => AZ
        53 => BA
        54 => BB


        BAC

        2 * 26 ^2 +  1 * 26 ^ 1 + 3 * 26 ^ 0
        
        1352 + 26 + 3 = 1381

      26| 1381
        -------
     26 |   53 -> 3
        ------ 
             2 -> 1
     26|
        -------
             0 -> 2

        '''

        ret = []

        while columnNumber:
            columnNumber -= 1
            leftover = columnNumber % 26
            ret.append(leftover)
            columnNumber = columnNumber // 26
        
        return ''.join([chr(ret[i] + ord('A')) for i in range(len(ret)-1, -1, -1)])
            
        
        
            
