class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        1. make hash_map
        {
            0 : [1]
            1 : [0, 2]
            2 : [1]
            3 : [4]
            4 : [3]
        }

        2. using dfs, travel and count

        3. return count
        '''
        # 1. make hash_map
        hash_map = defaultdict(list)
        
        for start, end in edges:
            hash_map[start].append(end)
            hash_map[end].append(start)
        
        # 2. using dfs, travel and count
        visited = set()
        def dfs(current_node: int, previous_node: int):
            if current_node in visited:
                return
                
            visited.add(current_node)

            if current_node in hash_map:
                for new_node in hash_map[current_node]:
                    if new_node == previous_node:
                        continue
                    
                    dfs(new_node, current_node)
                    
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        
        return count