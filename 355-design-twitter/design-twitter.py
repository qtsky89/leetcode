class Twitter:

    def __init__(self):
        '''
        tweet_map = {
            23:     [(99, 52525)]
           (user_id): (time, tweet_id)
        }
        
        follow_map = {
            23 : {24, 221, 22323}
            (followee)
        }
        '''

        self.tweet_map: dict[int, list[tuple[int, int]]] = {}
        self.follow_map: dict[int, set[int]] = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId in self.tweet_map:
            self.tweet_map[userId].append((self.time, tweetId))
        else:
            self.tweet_map[userId] = [(self.time, tweetId)]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        folowee_ids ={userId}
        if userId in self.follow_map:
            folowee_ids |= self.follow_map[userId]

        tweets = []
        for folowee_id in folowee_ids:
            if folowee_id in self.tweet_map:
                tweets += self.tweet_map[folowee_id]
        
        tweets.sort(reverse=True, key = lambda x: x[0])

        ret = []

        for i in range(min(len(tweets), 10)):
            ret.append(tweets[i][1])
        
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].add(followeeId)
        else:
            self.follow_map[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)