class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        {
            0 : [1, 3]
            1 : [2]
            3 : [1]
        }

        count = [0, 0, 0, 0]
                 0  2  1  1
        '''
        
        count = [0] * numCourses
        # make adjacent_map
        adjacent_map = {}
        for end, start in prerequisites:
            if start in adjacent_map:
                adjacent_map[start].append(end)
            else:
                adjacent_map[start] = [end]
            
            count[end] += 1

        q = deque()
        visited = set()

        for i in range(len(count)):
            if count[i] == 0:
                q.append(i)
        
        while q:
            item = q.popleft()

            visited.add(item)

            if item in adjacent_map:
                for new_item in adjacent_map[item]:
                    if new_item not in visited:
                        count[new_item] -= 1
                        if count[new_item] == 0:
                            q.append(new_item)
        
        return len(visited) == numCourses
                
        
        
        
            
        


        
        



