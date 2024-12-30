from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        example2.
            hand = [1, 2, 3, 4, 5] groupSize=4

            [1, 2, 3, 4]
            [1, 2, 3, 4, 5, 6, 7, 8]

            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] => 

            1, 2, 3, 4
            5, 6, 7, 8

        '''

        if len(hand) % groupSize != 0:
            return False
        
        '''
        c = {
            1: 1
            2: 2
            3: 2
            4: 1
            6: 1
            7: 1
            8: 1
        }

        '''
        c = Counter(hand)

        cur_count = 0

        smallest = min(c.keys())
        q = deque([smallest])

        while q:
            item = q.popleft()
            cur_count += 1

            c[item] -=1
            if c[item] == 0:
                del c[item]
            
            if cur_count == groupSize:
                cur_count = 0
                if c:
                    smallest = min(c.keys())
                    q.append(smallest)
                continue
            
            if item+1 not in c:
                return False
            
            q.append(item+1)
        
        return True

                

        
        return True