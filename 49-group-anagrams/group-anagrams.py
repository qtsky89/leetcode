class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        step1.

        hash_map = {
            'aet' : ['eat', 'tea' ...],
            'abt' : ['bat']
            ..
        }

        step2. return list(hash_map.values())
        '''

        hash_map = {}

        for s in strs:
            k = ''.join(sorted(s))

            if k in hash_map:
                hash_map[k].append(s)
            else:
                hash_map[k] = [s]
        return list(hash_map.values())
        