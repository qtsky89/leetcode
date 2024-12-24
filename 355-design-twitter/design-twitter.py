'''
self._follow_map = {
    1 : {1, 2, 3, 4}
            ^  ^  ^
    }
self._tweetMap = {
    1 : [1, 2, 3]
               ^
}
'''


class Twitter:
    def __init__(self) -> None:
        self._follow_map: dict[int, set[int]] = {}
        self._tweet_map: dict[int, tuple[int, int]] = {}
        self._time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._time += 1
        if userId in self._tweet_map:
            self._tweet_map[userId].append((self._time, tweetId))
        else:
            self._tweet_map[userId] = [(self._time, tweetId)]
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # folloeeIds
        followeeIds = [userId]
        if userId in self._follow_map:
            followeeIds.extend(list(self._follow_map[userId]))

        all_tweets: list[tuple[int, int]] = []
        for user in followeeIds:
            if user in self._tweet_map:
                all_tweets.extend(self._tweet_map[user])
        
        all_tweets.sort(key=lambda x: x[0], reverse=True)

        ret = []
        for i in range(min(10, len(all_tweets))):
            ret.append(all_tweets[i][1])
        return ret


        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self._follow_map:
            self._follow_map[followerId].add(followeeId)
        else:
            self._follow_map[followerId] = {followeeId}


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self._follow_map:
            self._follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)