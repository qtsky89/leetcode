from collections import Counter, deque


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        hand_map = {
            1: 1
            2: 2
            3: 2
            4: 1
            6: 1
            7: 1
            8: 1
        }

        '''
        hand_map = Counter(hand)
        
        min_key = min(hand_map.keys())

        q = deque([(min_key, 1)])

        while q:
            item, current_count = q.popleft()

            hand_map[item] -= 1

            if hand_map[item] == 0:
                del hand_map[item]
            
            if current_count == groupSize and hand_map:
                min_key = min(hand_map.keys())
                q.append((min_key, 1))
            elif current_count < groupSize:
                if (item + 1) not in hand_map:
                    return False
                
                q.append((item+1, current_count+1))
        
        return True

        
        