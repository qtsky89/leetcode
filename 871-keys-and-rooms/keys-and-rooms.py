from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        example1.

        n = 4
        
        0 1 2 3

        0 is unlocked
        coudln't enter without key

        1 2 3 []
        ^           key: 1
          ^         key: 2
            ^       key: 3
              ^ 

        example2.
        [1,3] [3,0,1] [2] [0]
         ^                       key: 1, 3
                 ^               key: 1, 0, 3           
                           ^     key: 1, 0, 3
        '''

        q = deque([0])

        visited = set()
        while q:
            key = q.popleft()
            visited.add(key)

            for key in rooms[key]:
                if key not in visited:
                    q.append(key)

        return len(visited) == len(rooms)
            
        