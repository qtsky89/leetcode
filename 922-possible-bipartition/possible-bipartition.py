class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        Bipartite graph


        colors = [0 0 0 0] BLUE: 1, RED: -1

        1. change this colors array,when processing dislikes

        2. it's already occupied, and has different color, return False

        return True
        '''

        adjacent_map = defaultdict(list)
        for a, b in dislikes:
            adjacent_map[a].append(b)
            adjacent_map[b].append(a)
        colors = defaultdict(int)

        ret = True
        # it will update the color
        def dfs(current_people: int, current_color: int) -> None:
            nonlocal ret
            if ret is False:
                return

            colors[current_people] = current_color

            for dislike_people in adjacent_map[current_people]:
                # change ret
                if colors[dislike_people] != 0 and colors[dislike_people] != (current_color * (-1)):
                    ret = False
                    return
                
                if colors[dislike_people] == 0:
                    dfs(dislike_people, current_color * (-1))
        
        for i in range(1, n+1):
            if colors[i] == 0:
                dfs(i, 1)
        
        return ret

        
