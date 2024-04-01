class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        a / b = 2
        b / c = 3

        queries 
        a / c
        b / a
        a / e
        a / a
        x / x


        {
            a : [(b, 2)]
            b : [(a, 1/2), (c, 3)]
            c : [(a, 1/3)]
        }
        '''

        hash_map = defaultdict(list)

        for i in range(len(equations)):
            start, end = equations[i]
            value = values[i]

            hash_map[start].append((end, value))
            hash_map[end].append((start, 1/value))
                
        q = deque()

        ret = [-1.0] * len(queries)

        for index, (start, end) in enumerate(queries):
            q.append([start, end, start, 1.0, set(), index])
        
        while q:
            start, end, current_var, current_data, visited, index = q.popleft()
            visited.add(current_var)

            # end!
            if current_var == end and current_var in hash_map:
                ret[index] = current_data
                continue
            
            if current_var in hash_map:
                for next_var, next_data in hash_map[current_var]:
                    if next_var not in visited:
                        q.append([start, end, next_var, current_data*next_data, set(visited), index])
            
        return ret

            

