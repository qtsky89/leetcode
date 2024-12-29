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

        adjacent_map = defaultdict(list) # time: O(1)
        count_map = {i: 0 for i in range(numCourses)} # time: O(V), space: O(V)

        # time: O(E), space: O(E)
        for end, start in prerequisites:
            adjacent_map[start].append(end)

            count_map[end] += 1
        
        # O(V)
        visited = set()

        # q = [0]
        q = deque()

        # time: O(V), space: O(V)
        for key in count_map:
            if count_map[key] == 0:
                q.append(key)
        
        # time: O(V)
        while q:
            # item = 0
            item = q.popleft()
            visited.add(item)

            for next_course in adjacent_map[item]:
                count_map[next_course] -= 1

                if count_map[next_course] == 0:
                    q.append(next_course)

        return len(visited) == numCourses

        # time complexity: O(V+E), space complexity: O(V+E)
        

        