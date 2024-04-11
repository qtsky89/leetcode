class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        '''
        preferences =[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
        paris = [[0, 1], [2, 3]]

        friend   preference
        0         [1, 2, 3]
        1         [3, 2, 0]
        2         [3, 1, 0]
        3         [1, 2, 0]


        pairs = [0, 1] [2, 3]

        dic = {
            0 : ()
            1 : (3, 2) V
            2 : ()
            3 : (1)
        }

        1 => 3
        3 => 1

        => unhappy
        '''

        dic = {}

        for x, y in pairs:
            x_index = preferences[x].index(y)
            dic[x] = set(preferences[x][:x_index])

            y_index = preferences[y].index(x)
            dic[y] = set(preferences[y][:y_index])
        
        count = 0 
        for key in dic:
            for v in dic[key]:
                if key in dic[v]:
                  count += 1 # unhappy
                  break
        return count  


        
        

        
    
        

        return count