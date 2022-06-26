class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        if you were to turn nums into a min heap of size k, you always have access to the k'th largest
        popping and pushing to a heap can run in log(n) time
        need to heapify nums
        if nums is larger than k, pop off the heap n - k times, leaving the k largest
        """
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(nums) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        push the val to the heap, and then pop 
        this will put the val in sorted order, but the heap will be of size k + 1
        then when you pop, the heap will be back to size k
        that element when you pop again will be the new k'th largest
        don't care about min elements, so that's why we can always pop the min from the heap
        """
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)