from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        adjacent_map = {
            a : (b, 2.0)
            ^    ^
            b : (a, 0.5)
            ...
        }

        [a, c]
         ^  ^


        '''

        adjacent_map = {}

        for index, (start, end) in enumerate(equations):
            if start not in adjacent_map:
                adjacent_map[start] = [(end, values[index])]
            else:
                adjacent_map[start].append((end, values[index]))
            if end not in adjacent_map:
                adjacent_map[end] = [(start, 1/values[index])]
            else:
                adjacent_map[end].append((start, 1/values[index]))

        def dfs(current_char: str, end_char: str, current_cal: float, visited: set[str]) -> float:
            if current_char not in adjacent_map:
                return -1.0
            
            if current_char == end_char:
                return current_cal
            
            visited.add(current_char)
            
            for next_char, value in adjacent_map[current_char]:
                if next_char not in visited:
                    ret = dfs(next_char, end_char, current_cal * value, visited)
                    if ret != -1.0:
                        return ret
            return -1.0

        ret = []
        for start, end in queries:
            ret.append(dfs(start, end, 1, set()))
        
        return ret