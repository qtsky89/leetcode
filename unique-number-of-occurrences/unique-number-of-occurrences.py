from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # {1:3, 2: 2, 3:1}
        c = Counter(arr)
        
        count_set = set()

        for v in c.values():
            if v in count_set:
                return False
            else:
                count_set.add(v)
        
        return True
        