class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        step1.
        {
            i : 2
            love: 2
            leetcode: 1
            coding: 1
        }

        step2.
        heap = [[-2, i] [-2, love] [1, leetcode] [1, coding]]

        step3.
        ret = [i, love, ...]
        '''

        # step1. counter
        c = Counter(words)

        # step2. heap
        heap = []
        for key, value in c.items():
            heapq.heappush(heap, [-value, key])
        
        # step3. make ret
        ret = []
        while k > 0:
            _, key = heapq.heappop(heap)
            ret.append(key)
            k -= 1
        
        return ret

        

        