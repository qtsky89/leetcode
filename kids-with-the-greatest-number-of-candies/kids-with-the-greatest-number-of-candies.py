class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # candies = [4,2,1,1,2]
        # extra_candies = 1

        # max_candy_from_kid = 4
        max_candy_from_kid = max(candies)

        ret = [False] * len(candies)

        for i in range(len(ret)):
            ret[i] = True if candies[i] + extraCandies >= max_candy_from_kid else False

        return ret
        