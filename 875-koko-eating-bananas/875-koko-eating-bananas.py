class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        after deciding k, have to take up the whole hour even if there are bananas left, and continue eating the pile after the hour
        this means that if there are less than k bananas, koko will sit there and wait for the hour after eating all the bananas
        
        can choose any k value from 1 (1 bph) up to the max pile in the array (could be 30bph)
        for each k value, go through the piles array and calcuate how many hours it would take to eat all bananas
            if the hours it would take is greater than h, need to choose a lower k value
            if the hours it would take is less than h, need to choose a higher k value
            
        GET HOURS WITH K:
        iterate through piles
        divide the num by chosen k value, and take the ceil
            - this is the how many hours it took to eat this pile
        add that to a run sum
        
        
        piles = [3,6,7,11], h = 8
                 1 1 2 2
        k = 6
        
        k value array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                       0  1  2  3  4  5  6  7  8  9  10
        """
        lo, hi = 1, max(piles)
        k = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            cur_hours = self.get_hours(piles, mid)
            if cur_hours <= h:
                k = mid
                hi = mid - 1
            elif cur_hours > h:
                lo = mid + 1
        return k
        
    def get_hours(self, piles, k):
        total_h = 0
        for bananas in piles:
            total_h += math.ceil(bananas / k)
        return total_h
