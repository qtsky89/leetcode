class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # flowerbed = [1 0 0 0 1]
        # n = 2

        # I can reduce the n when flowerbed[i-1] = 0 and flowerbed[i] != 1 only

        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
       
        return False