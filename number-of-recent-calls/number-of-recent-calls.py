from bisect import bisect_left

class RecentCounter:
    def __init__(self):
        self._times: list[int] = []
        
    def ping(self, t: int) -> int:
        if len(self._times) == 0:
            self._times.append(t)
            return 1

        # [start, end] [t-3000, t]

        # second round
        # self._times = [1]
        # t = 100
        # [-2900, 100]
        
        start = t-3000 # -2900
        left_index = bisect_left(self._times, start) # 0

        end = t # 100
        right_index = bisect_left(self._times, end) # 1

        self._times.append(t)

        return right_index-left_index+1









        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)