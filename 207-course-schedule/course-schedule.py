class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        1. make hash_map
        hash_map = {
            start: [end]
        }

        2. can travel only no prerequisite 

        3. remove line when travel

        4. return true if hash_map is empty else return false
        '''
        hash_map = {}
        indirect_count = {i: 0 for i in range(numCourses)}

        # 1. make hash_map, indirect count
        for prerequisite in prerequisites:
            end, start = prerequisite

            if start in hash_map:
                hash_map[start].append(end)
            else:
                hash_map[start] = [end]
            
            indirect_count[end] += 1
            
        
        # 2. can travel only no prerequisite 
        q = deque()
        for i in range(numCourses):
            if indirect_count[i] == 0:
                q.append(i)
        
        while q:
            item = q.popleft()

            if item in hash_map:
                for new_item in hash_map[item]:
                    indirect_count[new_item] -= 1

                    if indirect_count[new_item] == 0:
                        q.append(new_item)
                del hash_map[item]
        
        return len(hash_map) == 0
        
                

            

            