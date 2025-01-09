class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        numCourses = 4 (0, 1, 2, 3)

        prerequisites = [[1, 0], [1, 2], [2, 0], [0, 3]]

        queries = [[1, 0], [1, 2]]
        
        adjacent_map = {
            0: [3]
            1: [0, 2]
            2: [0]
            3: []
        }

        course_map = {
            0 : {3}
            1 : {0, 2, 3}
            2 : {0, 3}
            3 : {}
        }
        '''

        adjacent_map = {i: [] for i in range(numCourses)}
        for start, end in prerequisites:
            adjacent_map[start].append(end)

        course_map = {i: set() for i in range(numCourses)}
        def dfs(current_course: int) -> set[int]:
            if not course_map[current_course]:
                course_map[current_course] |= set(adjacent_map[current_course])

                for next_course in adjacent_map[current_course]:
                    course_map[current_course] |= dfs(next_course)
            
            return course_map[current_course]
        
        for i in range(numCourses):
            dfs(i)

        ret = []
        for start, end in queries:
            ret.append(end in course_map[start])
        
        return ret