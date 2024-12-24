from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        numCourses = 5, prerequisites = [1, 0] [4, 0] [3, 4] [3, 2]

        make adjacent_map
        adjacent_map = {
            0 : [1, 4]
            2 : [3]
            4 : [3]
        }

        count_map = {
            0 : 0
            1 : 1
            2 : 0
            3 : 1
            4 : 1
        }

        always go through when count is zero

        if we could visit all courses, return True else return False
        '''

        adjacent_map: dict[int, list[int]] = {}
        count_map: dict[int, int] = {i: 0 for i in range(numCourses)}

        # time complexity: O(M) M => number of prerequisites
        for end, start in prerequisites:
            if start in adjacent_map:
                adjacent_map[start].append(end)
            else:
                adjacent_map[start] = [end]
            
            count_map[end] += 1
        
        visited = set()

        q = deque()
        # time complexity: O(N)
        for key, count in count_map.items():
            if count == 0:
                q.append(key)

        # 0, 2
        # O(N+M)
        while q:
            # 0
            current_course = q.popleft()
            visited.add(current_course)
            
            if current_course in adjacent_map:
                for next_course in adjacent_map[current_course]:
                    if next_course not in visited:
                        count_map[next_course] -= 1
                        if count_map[next_course] == 0:
                            q.append(next_course)

        return len(visited) == numCourses

        '''
        time complexity: O(N+M) N=> numrCourses, M => prerequisites length
        space complecity: O(N+M) N=> numrCourses, M => prerequisites length
        '''