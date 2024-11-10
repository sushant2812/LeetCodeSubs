from collections import defaultdict
class Twitter:

    def __init__(self):
        self.userFollowing = defaultdict(list)
        self.userTweets = defaultdict(list)
        self.tweets=[]
        self.timer=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.timer,tweetId))
        self.timer+=1

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowing[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowing[followerId]:
            self.userFollowing[followerId].remove(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetheap=[]
        following=self.userFollowing[userId][:]
        following.append(userId)
        visited=set()
        for followeeId in following:
            for time,idx in self.userTweets[followeeId]:
                if idx in visited:
                    continue
                heappush(tweetheap,(time,idx))
                visited.add(idx)
                if len(tweetheap)>10:
                    heappop(tweetheap)
        tweetheap.sort(reverse=True)
        return[i[1] for i in tweetheap]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)