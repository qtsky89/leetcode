class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        example1.

        nums1 = [1, 3, 3, 2]
        nums2 = [2, 1, 3, 4]
        k = 3

        get k element from nums1 * get min value from nums2 (k element)

        want to get maximum value and return that value

        nums1 => I want to get maximum value
        nums2 => I want to avoid min value

        [1, 2] [3, 1] [3, 3] [2, 4]

        after sort by nums2
      
        [2, 4] [3, 3] [1, 2] [3, 1] 


        case 2 is minimum
        2, 3 => maximum 2 of the these value

        case 1 is minimum
        2, 3, 1  => maximum 2 of the these value

        ..
        '''

        num_pack = []
        for i in range(len(nums1)):
            num_pack.append([nums1[i], nums2[i]])
        
        num_pack.sort(key=lambda p:p[1], reverse=True)
        # nums_pack =[ [2, 4] [3, 3] [1, 2] [3, 1] ]

        min_heap = []
        tmp_sum = 0
        max_ret = 0

        for x, y in num_pack:
            heapq.heappush(min_heap, x)
            tmp_sum += x

            if len(min_heap) > k:
                tmp_sum -= heapq.heappop(min_heap)
            
            if len(min_heap) == k:
                max_ret = max(max_ret, tmp_sum * y)
        return max_ret
                
            
        