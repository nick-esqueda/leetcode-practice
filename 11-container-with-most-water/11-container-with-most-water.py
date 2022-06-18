class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        [1,8,6,2,5,4,8,3,7]

        keep track of the max area with a var
        to calc area, multiply (2nd index - 1st index) * lowest height between the 2 lines

        two pointers on either end to define bounds
        whichever line is taller, move the other line up one
        """
        i, j = 0, len(height) - 1
        max_area = float('-inf')
        while i != j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return max_area
        
            