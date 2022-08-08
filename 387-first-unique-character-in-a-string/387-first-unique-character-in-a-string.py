class Solution:
    def firstUniqChar(self, strings: str) -> int:
        c = Counter(strings)
        
        for i in range(len(strings)):
            if c[strings[i]] == 1:
                return i
        
        return -1
            