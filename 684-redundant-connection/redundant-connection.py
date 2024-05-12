class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        # initial state
        parent = [0, 1, 2, 3]
        rank =   [0, 1, 1, 1]

        # [1, 2]
        parent = [0, 1, 1, 3]
        rank =   [0, 2, 1, 1]

        # [1, 3]
        parent = [0, 1, 1, 1]
        rank =   [0, 3, 1, 1]

        # [2, 3]
        parent = [0, 1, 1, 1]
        rank =   [0, 3, 1, 1]
        '''
        '''
        # initial state
        parent = [0, 1, 2, 3]
        rank =   [0, 1, 1, 1]
        '''
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def find(current: int) -> int:
            while current != parent[current]:
                current = parent[current]
            return current

        def union(x: int, y: int) -> bool:
            p1, p2 = find(x), find(y)

            # it'a already connected
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]