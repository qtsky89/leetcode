from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        adjacent_map = {
           0 : [1]
           1 : [2]
           3 : [2]
        }

        count_map = {
            0 : 0 <=
            1 : 1
            2 : 2
            3 : 1
        }

        '''

        adjacent_map = defaultdict(list)
        count_map = {i: 0 for i in range(numCourses)}

        for end, start in prerequisites:
            adjacent_map[start].append(end)

            count_map[end] += 1
        
        visited = set()

        # q = [0]
        q = deque()

        for key in count_map:
            if count_map[key] == 0:
                q.append(key)
        
        while q:
            # item = 0
            item = q.popleft()
            visited.add(item)

            # 
            for next_course in adjacent_map[item]:
                count_map[next_course] -= 1

                if count_map[next_course] == 0:
                    q.append(next_course)

        return len(visited) == numCourses
        

        