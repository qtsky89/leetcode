class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        example. gain =    [ -5, 1, 5, 0, -7 ]
                 altitude =[  0 -5 -4 -4] 

                 altitude[0] = 0
                 altitude[1] = altitude[0] + gain[0] = -5
                 altitude[2] = altitude[1] + gain[1] = -4
                 altitude[3] = altitude[2] + gain[2] =  1

        altitude[0] = 0
        '''

        altitude = [0] * (len(gain)+1)

        max_altitude = 0
        for i in range(1, len(altitude)):
            altitude[i] = altitude[i-1] + gain[i-1]

            max_altitude = max(max_altitude, altitude[i])

        return max_altitude
        
