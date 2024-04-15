class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        s = b a b
       
        t = a b a
            ^
        '''

        s_counter = Counter(s)
        t_counter = Counter(t)

        ret = 0
        for key in t_counter:
            if key in s_counter and t_counter[key] > s_counter[key]:
                ret += t_counter[key] - s_counter[key]
            elif key not in s_counter:
                ret += t_counter[key]

        return ret