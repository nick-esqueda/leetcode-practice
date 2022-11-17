class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return self.mono_dec_queue(nums, k)
        return self.max_heap(nums, k)


    def max_heap(self, nums: List[int], k: int) -> List[int]:
        output = []
        maxes = []

        for R, num in enumerate(nums):
            heapq.heappush(maxes, (-num, R))

            L = R - k + 1
            while maxes[0][1] < L:
                heapq.heappop(maxes)

            if R >= k - 1:
                output.append(-maxes[0][0])

        return output
        

    def mono_dec_queue(self, nums: List[int], k: int) -> List[int]:
        output = []
        max_idxs = deque()

        def add_max_to_deque(num, idx):
            while max_idxs and nums[max_idxs[-1]] <= num:
                max_idxs.pop()
            max_idxs.append(idx)

        # MAIN ALGORITHM:
        for R, num in enumerate(nums):
            add_max_to_deque(num, R) # add num's idx to deque.

            L = R - k + 1
            if max_idxs[0] < L: # remove OOB indices.
                max_idxs.popleft()

            if R >= k - 1: # if window has reached size k:
                curr_max = nums[max_idxs[0]]
                output.append(curr_max) # start appending.

        return output




