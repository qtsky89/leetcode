class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        k=3, n=7

        1 + 2 + 4 = 7

        k=3, n=9

        1, 2, 6
        1, 3, 5
        2, 3, 4
    
        '''

        q = deque()
        
        for i in range(1, n):
            q.append([[i], i])
              
        ret = []
        while q:
            item, total = q.popleft()

            if len(item) == k and total == n:
                ret.append(item)
                continue
            
            if len(item) == n:
                continue

            for i in range(item[-1]+1, 10):
                if total + i <= n:
                    q.append([[*item, i], total + i])
        return ret
            




