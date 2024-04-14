class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        '''

        preferences [
        0   [1 3 2]
        1   [2 3 0]
        2   [1 3 0]
        3   [0 2 1]
        ]

        more [
        0    [1 3]
        1    [2]
        2    [1 3]
        3    [0 2]
        ]
        '''

        more_preferable = [None] * n

        # pair1 = 0, pairs2 = 1
        for pair1, pair2 in pairs:
            for preference in preferences:
                index = preferences[pair1].index(pair2)
                more_preferable[pair1] = set(preferences[pair1][:index])
                
                index = preferences[pair2].index(pair1)
                more_preferable[pair2] = set(preferences[pair2][:index])
        
        unhappy_count = 0
        for i in range(len(more_preferable)):
            if not more_preferable:
                continue
            
            for j in more_preferable[i]:
                if i in more_preferable[j]:
                    unhappy_count += 1
                    break
        return unhappy_count
