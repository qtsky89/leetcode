class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = 1
        ()

        n = 2
        (())
        ()()

        n = 3
        ((()))
        ()()()
        (()())
        ()))((
        '''

        
        q = deque([['', 0, 0]])

        ret = []
        while q:
            item, left, right = q.popleft()

            if len(item) > n*2 or left > n or right > n:
                continue

            if len(item) == n*2:
                ret.append(item)
            
            q.append([item+'(', left+1, right])

            if right+1 <= left:
                q.append([item+')', left, right+1])
        
        return ret

        