class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        def dfs(current_node: int, current_work: list[int], visited: set[int]) -> None:
            current_work.append(current_node)
            visited.add(current_node)

            # it's dead end
            if current_node == len(graph)-1:
                ret.append(current_work)
                return
            
            # current_node=0, next_node = 1, 2
            for next_node in graph[current_node]:
                dfs(next_node, list(current_work), set(visited))
            
        dfs(0, [], set())

        return ret