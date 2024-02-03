from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        example1.

        a / b , b / c
        2.0       3.0

        a / c, b /a, a/ e, a / a, x / x

        we couldn't get them answer return -1

        
        a / b = 2
        b / c = 3

        a / c = 6

        # step1. make these hash_map
        {
           a : [ [b, 2.0], [d, 5.0] ]
           b : [ [c, 3.0] ]
        }

        # step2. process every query using bfs
        a -> b -> c

        # step3. if we found end value, add to the result, if we coudn't return -1
        '''

        # step1. make these hash_map
        hash_map = {}
        # start = a, end = b
        for i in range(len(equations)):
            start, end = equations[i]
            if start in hash_map:
                hash_map[start].append([end, values[i]])
            else:
                hash_map[start] = [[end, values[i]]]
            
            if end in hash_map:
                hash_map[end].append([start, 1/values[i]])
            else:
                hash_map[end] = [[start, 1/values[i]]]
        
        # step2. process every query using bfs
        for i in range(len(queries)):
            queries[i].append(1)
            queries[i].append(i)
            queries[i].append(set())

        ret = [-1] * len(queries)
        q = deque(queries)
        while q:
            # key = a, end_value = c, current = 1
            key, end_value, current, i, visited =  q.popleft()

            if key in hash_map and key == end_value:
                ret[i] = current
                continue
            visited.add(key)

            if key in hash_map:
                for next_key, next_value in hash_map[key]:
                    if next_key not in visited:
                        q.append([next_key, end_value, current * next_value, i, set(visited)])

        return ret






