class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        connections[i] = [ai, bi]

        a - > b

        city 0

        example1.

        0 <- 1 <- 3  <- 2
          <- 4 -> 5


        1. 1
        2. 1
        3. 0
        4. 0
        5. 1

        result = 3

        # step1 make hash map of connections
        connections_map = {
            0 : [1],
            1 : [3],
            2 : [3],
            4 : [0, 5],
        }

        neighbor_map = {
            0: [1, 4],
            1 : [0],
            1 : [3],
            3 : [1, 2],
            2 : [3]
            4 : [0, 5]
            5 : [4]
        }

        # step2 use queue and bfs, see we can go to the city zero,
        if we hit the dead-end modify the route and increase the modfy_count

        # step3 return modify_count
        '''

         # step1 make hash map of connections
        connection_map = {}
        neighbor_map = {}

        for start, end in connections:
            if start not in connection_map:
                connection_map[start] = [end]
            else:
                connection_map[start].append(end)
        
            if start not in neighbor_map:
                neighbor_map[start] = [end]
            else:
                neighbor_map[start].append(end)
            
            if end not in neighbor_map:
                neighbor_map[end] = [start]
            else:
                neighbor_map[end].append(start)
        
        # step2 use queue and bfs, see we can go to the city zero,
        # if we hit the dead-end modify the route and increase the modfy_count

        # q = [0, 1, 2, 3, 4, 5]
        q = deque([0])
        count = 0
        visited = set()


        while q:
            # 0
            item = q.popleft()

            visited.add(item)

            for next_item in neighbor_map[item]:
                # next_item = 1, 4
                if next_item not in visited:
                    if next_item not in connection_map or item not in connection_map[next_item]:
                        count += 1
                    q.append(next_item)

        return count

            

            

            
            

