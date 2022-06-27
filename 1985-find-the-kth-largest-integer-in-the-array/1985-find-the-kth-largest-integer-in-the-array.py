class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        iterate over nums to find and delete the max k times - n^2
        sort array and take kth last index - nlogn
        heapify and pop from heap k times - n + klog(n)
        """
        heap = [-int(n) for n in nums]
        heapq.heapify(heap)
        
        while k > 1:
            heapq.heappop(heap)
            k -= 1
            
        return str(-heapq.heappop(heap))
        
        