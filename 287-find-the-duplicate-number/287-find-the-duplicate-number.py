class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        there are n + 1 nums in the array
        but, each num's value is between 1-n
        this means that there is a duplicate
        only one specific number will be repeated, but it could be repeated MANY times (>2)
        you need to find this number without using any extra space
        
        if you pretend that each num is pointing to another index in the list, you'll end up having at least two nums pointing
            to the same index
        if at least two things point to another thing, a cycle is formed and you can't exit once you're in the cycle
        if you can find the start of the cycle, that is the duplicate / thing that needs to be returned
        
        FLOYD'S ALGORITHM / LL cycle detection algorithm:
        using a slow+fast pointer, find the first intersection point
        then, using the slow pointer and another slow pointer starting at the very beginning, increment both until they intersect
        that intersection point is the start of the cycle (somehow, idk)
        
        if you treat each num as pointers to other indices, you can follow the pointers and eventually find the cycle
        """
        slow, fast = 0, 0
        first_iter = True
        while slow != fast or first_iter:
            first_iter = False
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow_2 = 0
        while slow != slow_2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            
        return slow_2
