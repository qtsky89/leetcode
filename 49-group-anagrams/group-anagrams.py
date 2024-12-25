from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        str = "eat"
        {
            'e' : 1
            'a' : 1
            't' : 1
        }

        ret = {
            counter : ["ate", "eat", "tea"]
        }
        '''

        ret_map: dict[str, list[str]] = {}

        for string in strs:
            c_str = ''.join(sorted(string))
            if c_str in ret_map:
                ret_map[c_str].append(string)
            else:
                ret_map[c_str] = [string]

        ret = [v for v in ret_map.values()]
        return ret
        