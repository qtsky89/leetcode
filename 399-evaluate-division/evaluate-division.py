class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        a / b = 2
        b / c = 3

        a / c => 6

        {
            a : [b, 2]
            b : [a, 1/2]
            ...
        }

        '''

        hash_map = {}

        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]

            if x in hash_map:
                hash_map[x].append([y, value])
            else:
                hash_map[x] = [[y, value]]
            
            if y in hash_map:
                hash_map[y].append([x, 1/value])
            else:
                hash_map[y] = [[x, 1/value]]

        q = deque()
        for index, query in enumerate(queries):
            q.append([index, query[0], query[1], 1, set()])

        ret = [-1] * len(queries)

        while q:
            index, current_char, end_char, current_cal, visited = q.popleft()

            if current_char == end_char and current_char in hash_map:
                ret[index] = current_cal
                continue
            
            if current_char not in visited:
                visited.add(current_char)
            
            if current_char in hash_map:
                for next_char, cal in hash_map[current_char]:
                    if next_char not in visited:
                        q.append([index, next_char, end_char, current_cal * cal, set(visited)])
        return ret
            
            


        