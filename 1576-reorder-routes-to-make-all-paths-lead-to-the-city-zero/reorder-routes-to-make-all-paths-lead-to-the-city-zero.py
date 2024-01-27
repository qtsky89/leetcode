from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {x: [] for x in range(n)}
        for x, y in connections:
            edges[x].append(y)

        neighbors = {city: [] for city in range(n)}
        for x, y in connections:
            neighbors[x].append(y)
            neighbors[y].append(x)

        visited = set()
        count = 0

        q = deque([0])
        while q:
            # 0
            item = q.popleft()
            visited.add(item)

            # neighbor = 1, 4 ...

            for neighbor in neighbors[item]:
                if neighbor not in visited:
                    if not (neighbor in edges and item in edges[neighbor]):
                        count += 1
                    q.append(neighbor)
        return count

        
        