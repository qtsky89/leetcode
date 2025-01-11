class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        arr = 9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9
              l       r
        '''

        if len(arr) == 1:
            return 1
        
        l, r = 0, 1
        prev_sign = ''
        max_turbulence_size = 1

        while r <= len(arr)-1:
            if arr[r-1] > arr[r] and prev_sign != '>':
                max_turbulence_size = max(max_turbulence_size, r-l+1)
                prev_sign = '>'
                r += 1
            elif arr[r-1] < arr[r] and prev_sign != '<':
                max_turbulence_size = max(max_turbulence_size, r-l+1)
                prev_sign = '<'
                r += 1
            elif arr[r-1] == arr[r]:
                prev_sign = '='
                l, r = r, r+1
            elif arr[r-1] > arr[r] and prev_sign == '>':
                prev_sign = '>'
                l, r = r-1, r+1
            elif arr[r-1] < arr[r] and prev_sign == '<':
                prev_sign = '<'
                l, r = r-1, r+1
        
        return max_turbulence_size