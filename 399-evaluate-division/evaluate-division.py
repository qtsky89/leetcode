class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        a / b =  2.0
        b / c = 3.0

        queries
            a / c => ?
            b / a =>
            a / e =>
            a / a =>
            x / x =>
        '''

        hash_table = defaultdict(list)

        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]

            # x / y = val
            hash_table[x].append([y, val])
            hash_table[y].append([x, 1 / val])
        
        q = deque()
        for i, query in enumerate(queries):
            # query = ['a', 'c']
            start, end = query
            
            # claculated value = 1
            q.append([start, end, i, 1, set()])
        
        ret = [-1] * len(queries)
        while q:
            current_char, end_char, ret_index, current_cal, visited = q.popleft()

            if current_char == end_char and hash_table[current_char] != []:
                ret[ret_index] = current_cal
                continue
            
            visited.add(current_char)
            
            for next_char, val in hash_table[current_char]:
                if next_char not in visited:
                    q.append([next_char, end_char, ret_index, current_cal * val, set(visited)])
            
        return ret
        
        
        
        
        

        
        
        