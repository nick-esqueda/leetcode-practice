class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        if you map every coord to it's distance from the origin, you can find k least distances and return those
        once you get all distances, group them with the coords in a list
        min heapify that list based on the distances
        pop k times to get k closest elements
        """
        def get_dist(coord):
            x1, y1 = coord
            x2, y2 = 0, 0
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        points = [(get_dist(coord), coord) for coord in points]
        heapq.heapify(points)
        
        closest = [heapq.heappop(points)[1] for i in range(k)]
        return closest
