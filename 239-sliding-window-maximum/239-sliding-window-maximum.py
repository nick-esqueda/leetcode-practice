class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        can use a double ended queue to keep track of the largest num in each window
        whenever a large number appears, pop off the BACK of the queue until there are no more numbers less than it
        if a smaller (or equal) number appears, put it on the back of the queue without popping
        always take the number at the left of the queue to add to result
        remove the max from the queue when it leaves the window (check for equality)
        doing it this way, you always ensure that what is at the left of the queue is the greatest num
            that you have seen so far
        """
        res = []
        q = deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            
            if r - l != k - 1:
                continue
                
            res.append(q[0])
            if nums[l] == q[0]:
                q.popleft()
            l += 1
            
        return res