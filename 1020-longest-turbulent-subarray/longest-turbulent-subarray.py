class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        arr = 9  4  2  10  7  8  8  1  9
                >  >  <   >  <  =  >  <
              l     r                                 2


        '''

        if len(arr) == 1:
            return 1

        l, r = 0, 1
        # previous_sign = > < =
        previous_sign = '='

        ret = 0
        while r <= len(arr)-1:
            if arr[r-1] < arr[r]:
                if previous_sign == '<':
                    l = r - 1
                previous_sign = '<'
            elif arr[r-1] > arr[r]:
                if previous_sign == '>':
                    l = r - 1    
                previous_sign = '>'
            elif arr[r-1] == arr[r]:
                l = r
                previous_sign = '='
            ret = max(ret, r-l+1)

            r += 1
        return ret