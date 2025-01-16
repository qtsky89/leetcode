class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        adjacent_map = {
            0 : [1]
            2 : [1]
            3 : [4]
            5 : []
        }

        count_map = {
            0 : 0
            2:  0
            1 : 2
            3 : 0
            4 : 1
            5 : 0
        }

        1. make this adjacent_map done
        2. make this count_map done
        3. make q and put the course that count 0 only
        4. keep doing that
        5. if we visited all the course, return True else False
        '''

        # 1. make this adjacent_map
        adjacent_map: defaultdict[int, list[int]] = defaultdict(list)
        count_map: dict[int, int] = {i: 0 for i in range(numCourses)}

        for end, start in prerequisites:
            adjacent_map[start].append(end)
            
            # 2. make this count_map    
            count_map[end] += 1
        
        # 3. make q and put the course that count 0 only
        q = deque()

        for course in count_map:
            if count_map[course] == 0:
                q.append(course)
        
        visited = set()
        # 4. keep doing that
        # q = [0, 2, 3, 5]
        while q:
            # 0
            course = q.popleft()

            visited.add(course)

            for next_course in adjacent_map[course]:
                count_map[next_course] -= 1

                if count_map[next_course] == 0:
                    q.append(next_course)


        # 5. if we visited all the course, return True else False
        return len(visited) == numCourses
        
        
