from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        counter = {
            i : 2
            love : 2
            ...
        }
        '''
        counter = defaultdict(int)

        for word in words:
            counter[word] += 1
        
        heap = []
        for key in counter:
            heapq.heappush(heap, [-counter[key], key])
        
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])

        return ret

        
        