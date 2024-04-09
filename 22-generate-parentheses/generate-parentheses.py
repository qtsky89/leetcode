class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        generate parentheses

        n = 3

        
        '''

        q = deque([['', 0, 0]])

        ret = []
        while q:
            current, left_count, right_count = q.popleft()

            if left_count == right_count == n:
                ret.append(current)
                continue
            
            if left_count > n:
                continue
            
            if left_count > right_count:
                q.append([current + ')', left_count, right_count+1])
            q.append([current+'(', left_count+1, right_count])
        
        return ret

        