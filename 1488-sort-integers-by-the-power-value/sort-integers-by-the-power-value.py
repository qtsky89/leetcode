'''
    1 => 1                        0
    2 => 2->1                     1
    3 => 3->10->5->16->8->4->2->1 7
'''

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}

        def dfs(i: int) -> int:
            if i in cache:
                return cache[i]
            
            # even number
            if i % 2 == 0:
                cache[i] = dfs(i/2)+1
            else:
                cache[i] = dfs(i*3+1)+1
            
            return cache[i]
        
        heap = []
        for i in range(lo, hi+1):
            heapq.heappush(heap, [dfs(i) , i])
        
        ret = 0
        while k > 0:
            ret = heapq.heappop(heap)
            k -= 1

        return ret[1]