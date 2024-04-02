class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        heapq.heapify(slots1)
        heapq.heapify(slots2)

        while slots1 and slots2:
            l1, r1 = slots1[0]
            l2, r2 = slots2[0]

            if (min(r1, r2) - max(l1, l2)) >= duration:
                return [max(l1, l2), max(l1, l2) + duration]
            
            if r1 < r2:
                heapq.heappop(slots1)
            else:
                heapq.heappop(slots2)
        return []

            