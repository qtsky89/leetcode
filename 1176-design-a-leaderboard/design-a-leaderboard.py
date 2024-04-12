class Leaderboard:
    def __init__(self):
        self.dic = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.dic:
            self.dic[playerId] += score
        else:
            self.dic[playerId] = score
        
    def top(self, K: int) -> int:
        heap = []

        for playerId in self.dic:
            heapq.heappush(heap, [-self.dic[playerId], playerId])
        
        ret = 0
        while K > 0:
            ret += (-heapq.heappop(heap)[0])
            K -= 1
        
        return ret

    def reset(self, playerId: int) -> None:
        del self.dic[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)