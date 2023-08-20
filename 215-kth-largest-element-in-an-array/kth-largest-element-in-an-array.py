from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      tmp_nums = [-n for n in nums]
      heapify(tmp_nums)

      while k > 0:
        item = heappop(tmp_nums)
        k -= 1
        
        if k == 0:
          return -item
        

      
      