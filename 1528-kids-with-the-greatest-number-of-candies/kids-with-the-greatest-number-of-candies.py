class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
        candies = [2,   3,   5,   1,   3]
        candies = [2,   6,   5,   1,   3]
                  true, true, 
        extraCandies = 3
        '''

        maxCandy = max(candies)
        ret = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy:
                ret[i] = True
        return ret