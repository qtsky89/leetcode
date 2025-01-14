from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hash_map = {
            'atn': ['eat']
            'bat': []
        }

        => list[list[str]]
        '''

        hash_map: defaultdict[str, list[str]] = defaultdict(list)

        for s in strs:
            hash_map[''.join(sorted(s))].append(s)
        
        ret = []
        for v in hash_map.values():
            ret.append(v)
        
        return ret