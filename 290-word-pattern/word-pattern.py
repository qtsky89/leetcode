class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        pattern_string_map = {
            'a' : 'dog',
            'b' : 'cat'
        }

        string_pattern_map = {
            'dog' : 'a',
            'cat' : 'b'
        }
        '''

        
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False

        pattern_string_map = {}
        string_pattern_map = {}
        
        for i in range(len(pattern)):
            # no matching case
            if pattern[i] not in pattern_string_map and s_list[i] not in string_pattern_map:
                pattern_string_map[pattern[i]] = s_list[i]
                string_pattern_map[s_list[i]] = pattern[i]
            elif (pattern[i] in pattern_string_map and s_list[i] in string_pattern_map) and \
                (pattern_string_map[pattern[i]] == s_list[i]) and \
                (string_pattern_map[s_list[i]] == pattern[i]):
                continue
            else:
                return False
        return True
                
            