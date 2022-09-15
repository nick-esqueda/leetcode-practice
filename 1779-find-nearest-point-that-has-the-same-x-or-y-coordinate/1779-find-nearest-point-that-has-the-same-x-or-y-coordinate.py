class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        point is "valid" if it has either the same x coord or the same y coord as where you are
        
        there may be multiple valid points,
        but, you want the one with the smallest distance from you
            if there are 2 that have the same dist, return the point that came first in the array
            
        you could loop through, and keep track of indices which you find a new shortest distance
        should probably keep the shortest distance itself in a variable also
        also should check to make sure that the new point shares either an x or a y
        """
        least_dist = float('inf')
        least_idx = 0
        for i, (x2, y2) in enumerate(points):
            if x != x2 and y != y2:
                continue
            dist = abs(x - x2) + abs(y - y2)
            if dist < least_dist: # this takes care of multiple shortest distances
                least_dist = dist
                least_idx = i
 
        return -1 if least_dist == float('inf') else least_idx
        
        