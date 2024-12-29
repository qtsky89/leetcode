class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        rank   : [0, 1, 1, 1]
            index    1  2  3
        parent : [0, 1, 2, 3]
            index    1  2  3

        [1, 2]
        rank   : [0, 2, 1, 1]
            index    1  2  3
        parent : [0, 1, 1, 3]
            index    1  2  3

        [1, 3]
        rank   : [0, 3, 1, 1]
            index    1  2  3
        parent : [0, 1, 1, 1]
            index    1  2  3

        [2, 3]
        rank   : [0, 3, 1, 1]
            index    1  2  3
        parent : [0, 1, 1, 1]
            index    1  2  3
        '''

        rank = [1] * (len(edges)+1)
        parent = [i for i in range(len(edges)+1)]

        # return parent
        def find(current: int) -> int:
            while parent[current] != current:
                current = parent[current]
            return current
        
        def union(x: int, y: int) -> bool:
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True

        for x, y in edges:
            ret = union(x, y)

            if not ret:
                return [x, y]
        