class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        s = p a p e r            t = t i t l e
                    ^                        ^
        
        {
            p -> t
            a -> i
            e -> l
            r -> e
        }
        '''

        visited = set()
        hash_map = {}
        for i in range(len(s)):
            if s[i] not in hash_map:
                if t[i] in visited:
                    return False
                    
                hash_map[s[i]] = t[i]
                visited.add(t[i])

            elif hash_map[s[i]] != t[i]:
                return False
        return True
                
            

        

