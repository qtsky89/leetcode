class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s_t = {}
        hash_map_t_s = {}
        
        for i in range(len(s)):
            if s[i] not in hash_map_s_t and t[i] not in hash_map_t_s:
                hash_map_s_t[s[i]] = t[i]
                hash_map_t_s[t[i]] = s[i]
                continue
                
            if (s[i] in hash_map_s_t and hash_map_s_t[s[i]] != t[i]) or (t[i] in hash_map_t_s and hash_map_t_s[t[i]] != s[i]):
                return False
        return True