class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key=lambda x:x[0])

        filtered_intervals: list[list[int]] = []

        for start, end in intervals:
            if not filtered_intervals:
                filtered_intervals.append([start, end])
                continue
            
            # is merged ?
            if filtered_intervals[-1][1] >= start:
                filtered_intervals[-1][0] = min(filtered_intervals[-1][0], start)
                filtered_intervals[-1][1] = max(filtered_intervals[-1][1], end)
            else:
                filtered_intervals.append([start, end])
        
        return filtered_intervals
            
            