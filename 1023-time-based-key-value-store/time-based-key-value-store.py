class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = [[timestamp, value]]
        else:
            self.hash_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        
        l, r = 0, len(self.hash_map[key])-1

        min_timestamp_value = ""
        while l <= r:
            mid = (l + r) // 2

            # bingo
            if self.hash_map[key][mid][0] == timestamp:
                min_timestamp_value = self.hash_map[key][mid][1]
                break
            elif self.hash_map[key][mid][0] > timestamp:
                r = mid - 1
            else:
                min_timestamp_value = self.hash_map[key][mid][1]
                l = mid + 1
        return min_timestamp_value

        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)