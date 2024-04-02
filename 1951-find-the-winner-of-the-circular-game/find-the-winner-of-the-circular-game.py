class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
            [2, 3, 4, 5, 1] 
        '''

        q = deque([i for i in range(1, n+1)])

        for _ in range(n-1):
            for _ in range(k-1):
                tmp = q.popleft()
                q.append(tmp)
            q.popleft()
        
        return q[0]
        
        
        

        