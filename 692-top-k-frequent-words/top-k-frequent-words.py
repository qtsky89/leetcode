
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        c = {
            i : 2
            love : 2
            leetcode: 1
            cofing: 1
        }
        '''
        c = Counter(words)

        heap = []
        for key in c:
            heapq.heappush(heap, [-c[key], key])

        
        ret = []
        while k > 0:
            _, w = heappop(heap)
            ret.append(w)
            k -= 1
        return ret