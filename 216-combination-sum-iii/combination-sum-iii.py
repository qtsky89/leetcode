class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        q = [{4} {2} {3} {1} ...]
        '''


        q = deque()
        for i in range(1, 10):
            q.append([[i],i])

        ret = []
        while q:
            item, current_sum = q.popleft()

            if len(item) == k and current_sum == n:
                ret.append(item)
                continue
            elif len(item) > k or current_sum > n:
                continue
            
            for i in range(item[-1]+1, 10):
                q.append([[*item, i], current_sum + i])

            
        
        return ret

        