class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        flowerbed = [1, 0, 0, 0, 1]
        n = 1 true

        flowerbed = [1, 0, 0, 0, 1]
        n = 2 false
        '''

        if not flowerbed:
            return False

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1

            if n <= 0:
                return True
        if n <= 0:
            return True
        return False
                