from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque([[0, [], set()]])

        ret = []
        while q:
            current, path, visited = q.popleft()

            path.append(current)
            visited.add(current)

            if current == len(graph)-1:
                ret.append(path)
                continue

            for next_val in graph[current]:
                if next_val not in visited:
                    q.append([next_val, list(path), set(visited)])
        return ret



        

        