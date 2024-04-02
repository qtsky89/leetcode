class Solution:
    def maxDepth(self, strings: str) -> int:
        '''
        s = 1+(2*3)+((8)/4) + 1
                1 + max(1, 2) 0 
        '''
        
        depth = 0
        open_count = 0
        for s in strings:
            match s:
                case '(':
                    open_count += 1
                case ')':
                    open_count -= 1
            
            depth = max(depth, open_count)
        return depth
        