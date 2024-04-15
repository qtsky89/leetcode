class Solution:
    def maxDepth(self, strings: str) -> int:
        '''
        '(' => counter += 1
        ')' => counter -= 1

        keep the max counter value

        example.1
            s = ( 1 + ( 2 * 3 ) + ( ( 8 ) / 4 ) ) + 1
                                                    ^
            counter = 0
        '''

        count = 0

        max_count = 0
        for s in strings:
            if s == '(':
                count += 1
            elif s == ')':
                count -= 1
            
            max_count = max(max_count, count)
        return max_count

        