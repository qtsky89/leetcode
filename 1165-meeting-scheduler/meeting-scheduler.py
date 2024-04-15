class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heapq.heapify(slots1)
        heapq.heapify(slots2)

        while slots1 and slots2:
            x_start, x_end = slots1[0]
            y_start, y_end = slots2[0]

            tmp_duration = min(x_end, y_end) - max(x_start, y_start)

            if tmp_duration >= duration:
                return [max(x_start,y_start), max(x_start,y_start) + duration]
            
            if x_end < y_end:
                heapq.heappop(slots1)
            else:
                heapq.heappop(slots2)
        return []

        