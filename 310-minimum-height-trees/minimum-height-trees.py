class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        adjacent_map = {
            0 : [1] # <= leaf
            1 : [0, 2, 3]
            2 : [1] # <= leaf
            3 : [1, 4]
            4 : [3] # <= leaf
        }

        if neighbor length is one => leaf

        '''

        if n == 1:
            return [0]

        # adjacent_map
        adjacent_map = defaultdict(list)
        
        for edge1, edge2 in edges:
            adjacent_map[edge1].append(edge2)
            adjacent_map[edge2].append(edge1)
        
        edge_count = {}      
        
        # put leaf node
        q = deque()
        for key, neighbor in adjacent_map.items():
            edge_count[key] = len(neighbor)

            # if neighbor length is one => leaf
            if len(neighbor) == 1:
                q.append(key)
        
        # go in side! using BFS
        visited = set()
        while q:
            if n <= 2:
                return list(q)

            for _ in range(len(q)):
                item = q.popleft()

                n -= 1

                for next_item in adjacent_map[item]:
                    edge_count[next_item] -= 1
                    # only leaf should put inside queue
                    if edge_count[next_item] == 1:
                        q.append(next_item)
            

                



            
        