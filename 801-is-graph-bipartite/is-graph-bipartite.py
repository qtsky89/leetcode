class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        colors = 0 0 0 0             # RED=1, BLUE=-1

        '''
        colors = [0] * len(graph)

        ret = True

        def dfs(i: int, color: int) -> None:
            nonlocal ret
            colors[i] = color

            if not ret:
                return

            for neighbor in graph[i]:
                if colors[neighbor] == colors[i]:
                    ret = False
                    return

                if colors[neighbor] == 0:
                    dfs(neighbor, -1*colors[i])

        for i in range(len(graph)):
            if not colors[i]:
                dfs(i, 1)
        
        return ret
