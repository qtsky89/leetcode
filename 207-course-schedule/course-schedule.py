from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        adjacent_map = {
            0 : [1, 2]
            1 : [3]
            2 : []
            3 : []
            4 : []
        }

        count_map = {
            0 : 0 <=
            1 : 1
            2 : 1
            3 : 1
            4 : 0 <=
        }

        '''

        # build adjacent_map
        adjacent_map: defaultdict[int, list[int]] = defaultdict(list)
        count_map: dict[int, int] = {}

        for i in range(numCourses):
            count_map[i] = 0

        for end, start in prerequisites:
            adjacent_map[start].append(end)
            count_map[end] += 1
        
        q = deque()

        for key, value in count_map.items():
            # leaf node
            if value == 0:
                q.append(key)

        visited = set()
        while q:
            # 0, 4
            item = q.popleft()
            visited.add(item)

            for next_item in adjacent_map[item]:
                count_map[next_item] -= 1

                if count_map[next_item] == 0 and next_item not in visited:
                    q.append(next_item)
        
        return len(visited) == numCourses
            
        
        

        

        

        