class Solution:
    # s = 'abcabcbb'
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        p1, p2, hash_map = 0, 0, {}
        
        max_length = 0
        while p2 <= len(s)-1:
            max_length = max(max_length, p2-p1+1)
            hash_map[s[p2]] = p2
            
            if p2+1 <= len(s)-1 and s[p2+1] in hash_map:
                p1 = hash_map[s[p2+1]] + 1 if hash_map[s[p2+1]] + 1 > p1 else p1
            p2 += 1
        
        return max_length
                
            
            
            
        
        
        
        