from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        adjacent_map = {
            1: [2, 3]
            2: [1, 4]
            3: [1]
            4: [2]          
        }

        # blue => 1, red => -1
        colors_map = {
            1 : 0
            2 : 0
            3 : 0
            4 : 0
        }

        if already has color and that color doesn't match:
            return False
        else
            return True
        '''

        adjacent_map = defaultdict(list)
        for a, b in dislikes:
            adjacent_map[a].append(b)
            adjacent_map[b].append(a)
        
        colors_map = defaultdict(int)

        ret = True
        # current_color => 1(BLUE), -1(RED) 0(WHITE)
        def dfs(current_people: int, current_color: int) -> None:
            nonlocal ret

            if not ret:
                return

            colors_map[current_people] = current_color

            for next_people in adjacent_map[current_people]:
                if colors_map[next_people] == current_color:
                    ret = False
                if colors_map[next_people] == 0:
                    dfs(next_people, current_color * (-1))
                
        for current_people in range(1, n):
            if colors_map[current_people] == 0:
                dfs(current_people, 1)
        
        return ret