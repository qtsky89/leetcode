from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        0 1 2 3 4 5 6
        '''

        visited = set()
        q = deque([0])
        while q:
            key = q.popleft()

            # len(rooms) = 4
            if key <= len(rooms) - 1 and  key not in visited:
                visited.add(key)
            
            next_keys = rooms[key]

            for k in next_keys:
                if k not in visited:
                    q.append(k)
            
        return len(visited) == len(rooms)



            