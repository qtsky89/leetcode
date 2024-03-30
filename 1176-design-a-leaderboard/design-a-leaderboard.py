'''
    {
        1 : 244,
        2 : 300,
        3 : 150,
        ...
    }

    [300, 2] [244, 1] [150, 3] ...
    
'''

from collections import defaultdict

class Leaderboard:
    def __init__(self):
        self._board = defaultdict(int)
        
    def addScore(self, player_id: int, score: int) -> None:
        self._board[player_id] += score
        
    def top(self, k: int) -> int:
        heap = []

        for value in self._board.values():
            heapq.heappush(heap, -value)
        
        ret = 0
        while k:
            ret += -(heapq.heappop(heap))
            k -= 1
        
        return ret

    def reset(self, player_id: int) -> None:
        self._board[player_id] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)