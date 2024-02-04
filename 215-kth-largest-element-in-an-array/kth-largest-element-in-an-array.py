class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minus_nums = [-n for n in nums]
        heapq.heapify(minus_nums)

        ret = 0
        for i in range(k):
            ret = - heapq.heappop(minus_nums)

        return ret
