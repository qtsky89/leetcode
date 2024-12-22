from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        ajacent_map = {
            1 : [2, 3]
            2 : [1, 4]
            3 : [1]
            4 : [2]
        }

        '''

        ajacent_map: defaultdict[int, list[int]] = defaultdict(list)

        for a, b in dislikes:
            ajacent_map[a].append(b)
            ajacent_map[b].append(a)

        colors = [0] * (n+1)

        ret = True
        def dfs(i: int, color: int) -> None:
            nonlocal ret
            if not ret:
                return
            colors[i] = color

            for neighbor in ajacent_map[i]:
                if colors[neighbor] == colors[i]:
                    ret = False
                    return

                if colors[neighbor] == 0:
                    dfs(neighbor, -1*colors[i])
        
        for i in range(n):
            if not colors[i]:
                dfs(i, 1)
        
        return ret