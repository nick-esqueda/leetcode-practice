class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-n for n in nums]
        # heapq.heapify(nums)
        # while k > 1:
        #     heapq.heappop(nums)
        #     k -= 1
        # return -heapq.heappop(nums)

        def _partition(left, right):
            pivot_num = nums[right]
            pi = left
            for j in range(left, right):
                if nums[j] <= pivot_num:
                    nums[pi], nums[j] = nums[j], nums[pi]
                    pi += 1
            nums[pi], nums[right] = nums[right], nums[pi]
            return pi
        
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = _partition(left, right)
            k_idx = len(nums) - k
            
            if pivot_idx > k_idx:
                right = pivot_idx - 1
            elif pivot_idx < k_idx:
                left = pivot_idx + 1
            else:
                return nums[pivot_idx]
        
        