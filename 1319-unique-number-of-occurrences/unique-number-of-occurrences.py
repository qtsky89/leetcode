class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}

        for i in range(len(arr)):
            if arr[i] in hash_map:
                hash_map[arr[i]] += 1
            else:
                hash_map[arr[i]] = 1
        
        return len(set(hash_map.values())) == len(list(hash_map.values()))
        