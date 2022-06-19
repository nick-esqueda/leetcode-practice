class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        set hi and lo to start and end of each row
        if the target is not within range, move on to the next row
        if the target is within range, binary search through that row
            if the num not found, return false, else true
        """
        def bin_search(lo, hi):
            while lo <= hi:
                mid = (hi + lo) // 2
                
                if row[mid] > target:
                    hi = mid - 1
                elif row[mid] < target:
                    lo = mid + 1
                else:
                    return True
            return False
                
        for row in matrix:
            lo = 0
            hi = len(row) - 1
            
            if row[lo] <= target <= row[hi]:
                return bin_search(lo, hi)
            
