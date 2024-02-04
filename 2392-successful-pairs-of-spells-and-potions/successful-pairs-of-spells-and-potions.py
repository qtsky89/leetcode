class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        spells = [5, 1, 3]    => n
        potions = [1, 2, 3, 4, 5] => m
        success = 7

        [5, 10, 15, 20, 25] => 4
        [1, 2, 3, 4, 5] => 0
        [3, 6, 9, 12, 15] => 3

        sucees = 7

        return [4, 0, 3]
        '''

        potions.sort()

        counts = [0] * len(spells)

        # [5, 10, 15, 20, 25]
        #  0       2       4
        for i, s in enumerate(spells):
             # l = 0, r = 4

            index = bisect.bisect_left(potions, success / s)

            counts[i] = len(potions) - index

        return counts