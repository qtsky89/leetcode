class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # gain = [ -5  1  5  0 -7 ]
        # ret =  [ -5 -4 1 1 -6] -> 1

        ret = [0] * (len(gain))

        max_altitude = 0
        for i in range(len(gain)):
            if i == 0:
                ret[i] = gain[0]
            else:
                ret[i] = gain[i] + ret[i-1]

            max_altitude = max(max_altitude, ret[i])
        
        return max_altitude