class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_t = Counter(t)
        counter_s = Counter(s)

        ret = 0
        for key in counter_t:
            tmp = (counter_t[key] - counter_s[key] if key in counter_s else counter_t[key])

            if tmp > 0:
                ret += tmp
        
        return ret