class Twitter:

    def __init__(self):
        """
        we want the tweets sorted in order of posted
        that way, we can just iterate through until we have 10 posts that have a userId that is in the user's following set
        """
        self.follows = defaultdict(set) # follower: set(followee, followee)
        self.tweets = [] 
        self.feed_heaps = {} # follower: maxheap() (based off of tweetId)(assuming tweetId's come in increasing order)
        
        
        """
        build a heap for each individual FOLLWER, so that whenever a followee posts something, you put it inside
            each follower's feed heap
        any time you want the 10 most recent, you can just grab the first 10 elements from that user's heap 
        """

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        if user doesn't exist, add it to follows
        will tweetId's come in always increasing order?
        if the userId is not in follows, add it
        add the tweet to tweets set
        """
        if userId not in self.follows:
            self.follows[userId].add(userId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        iterate through tweets until you have a collection of 10 posts that have a userId in the user's following set
        """
        following = self.follows[userId]
        tweets = []
        i = len(self.tweets) - 1
        while len(tweets) < 10 and i >= 0:
            user, tweet = self.tweets[i]
            if user in following:
                tweets.append(tweet)
            i -= 1
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)