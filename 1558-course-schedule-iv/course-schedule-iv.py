class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        adjacent_map = {
            0: []
            1: [0, 2]
            2: [0]
        }

        key: start course,
        value: all end course (recursively)

        cache_map = {
            0: {}
            1: {0, 2} <=
            2: {0}
        }

        if [1, 0] is it 0 is in the 1: {0, 2} ?
            True
        else
            False
        '''

        adjacent_map: defaultdict[int, list[int]] = defaultdict(list)

        for start, end in prerequisites:
            adjacent_map[start].append(end)
        
        cache_map: defaultdict[int, set[int]] = defaultdict(set)
        def dfs(course: int) -> set[int]:
            if course not in cache_map:
                for next_course in adjacent_map[course]:
                    cache_map[course].add(next_course)
                    cache_map[course] |= dfs(next_course)
            return cache_map[course]

        for i in range(numCourses):
            dfs(i)
        
        ret = []
        for start, end in queries:
            if end in cache_map[start]:
                ret.append(True)
            else:
                ret.append(False)
        
        return ret