class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # parent = [0, 1, 2, 3, 4, 5]
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n: int):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
            
        def union(x: int, y: int) -> bool:
            p1, p2 = find(x), find(y)

            # already in the connection
            if p1 == p2:
                return False
          
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]

        