class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        stones must be sorted so you don't have to rescan every time to get the 2 largest
        can use a max heap so that we always have access to the heaviest stone
        heapppop twice and subtract the smaller of the two from the larger
        if that difference is 0, do nothing
        otherwise, put the remainder back into the max heap
        keep doing all of this until the length of the max heap is <= 1
        return that last stone's weight, but if there is not last stone, return 0
        """
        stones = list(map(lambda x: x*-1, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            crushed = s1 - s2
            if crushed*-1 > 0:
                heapq.heappush(stones, crushed)
        
        return stones[0]*-1 if stones else 0