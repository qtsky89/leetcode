class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        colors = 0 0 0 0             # RED=1, BLUE=-1

        '''
        colors = [0] * len(graph)

        def dfs(i: int, color: int) -> bool:
            colors[i] = color

            for neighbor in graph[i]:
                if colors[neighbor] == colors[i]:
                    return False

                if not colors[neighbor]:
                    if not dfs(neighbor, -1*colors[i]):
                        return False
            return True

        for i in range(len(graph)):
            if not colors[i] and not dfs(i, 1):
                return False
        
        return True
