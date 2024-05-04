class Twitter:
    def __init__(self):
        '''
        data_map = {
            user_id: [[timeline, tweet_id]]
        }
        '''
        self.data_map = {}
    
        '''
        follow_map = {
            follower_id = {flowee_id1, flowee_id2 ...}
        }
        '''
        self.follow_map = {}
        self.time = 0
        
    def postTweet(self, user_id: int, tweet_id: int) -> None:
        if user_id in self.data_map:
            self.data_map[user_id].append([-self.time, tweet_id])
        else:
            self.data_map[user_id] = [[-self.time, tweet_id]]
        self.time += 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        followee_set = set()
        if user_id in self.follow_map:
            followee_set = self.follow_map[user_id]
        
        # include my self
        followee_set.add(user_id)

        heap = []

        for folowee_id in followee_set:
            if folowee_id in self.data_map:
                for item in self.data_map[folowee_id]:
                    heapq.heappush(heap, item)
        
        ret = []
        for _ in range(min(len(heap), 10)):
            timeline, tweet_id = heapq.heappop(heap)
            ret.append(tweet_id)
        
        return ret
        

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.follow_map:
            self.follow_map[follower_id].add(followee_id)
        else:
            self.follow_map[follower_id] = {followee_id}

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.follow_map:
            self.follow_map[follower_id].remove(followee_id)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)