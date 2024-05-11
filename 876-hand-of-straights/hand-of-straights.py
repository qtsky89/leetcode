class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:       
        # check leftover
        if len(hand) % groupSize != 0:
            return False

        '''
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        c = {
            1 : 1
            2 : 2
            3 : 2
            4 : 1
            6 : 1
            7 : 1
            8 : 1
        }

        '''

        c = Counter(hand)
        
        ret = []
        for _ in range(len(hand)):
            if not ret:
                min_key = min(c.keys())
                ret.append(min_key)
                c[min_key] -= 1

                if c[min_key] == 0:
                    del c[min_key]
            else:
                # no continuous value in counter
                if not (ret[-1] + 1) in c:
                    return False
                else:
                    ret.append(ret[-1] + 1)
                    c[ret[-1]] -= 1
                    if c[ret[-1]] == 0:
                        del c[ret[-1]]
            
            if len(ret) == groupSize:
                ret = []

        return True

        
        
            

