class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        2 1 14 12
        11 7 13 6

        (2, 11) (1, 7) (14, 13) (12, 6)
        after sort
        (14, 13) (2, 11) (1, 7) (12, 6)
        '''

        r: tuple[int, int] = []

        for i in range(len(nums1)):
            r.append([nums1[i], nums2[i]])

        r.sort(key=lambda x: x[1], reverse=True)
        
        max_ret = 0
        tmp_sum = 0
        min_heap = []
        for x, y in r:
            heapq.heappush(min_heap, x)
            tmp_sum += x

            if len(min_heap) > k:
                poped = heapq.heappop(min_heap)
                tmp_sum -= poped
            
            if len(min_heap) == k:
                max_ret = max(max_ret, tmp_sum * y)
        
        return max_ret




        return output