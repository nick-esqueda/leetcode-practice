class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        we are looking for k - we have to choose a k value.
        koko will sit there and take up the whole hour if the pile has < k bananas before moving to next pile.
        looking for the optimal speed/k so that you still eat ALL bananas in H hours.
        want the minimum k.
        
        ACCEPTABLE VALUES - k vals/speeds that let you finish less than h hours. (fast)
        UNACCEPTABLE VALUES - k vals/speeds that have you finish in more than h hours. (too slow)

        what is the range of k vals to search through?
        min: 1 banana/hr
        max: max(piles)/hr
        """

        def calculate_hours(speed: int):
            hours = 0
            for pile in piles:
                hours +=  ceil(pile / speed)
            return hours 

        lo = 1
        hi = max(piles)
        while lo < hi:
            speed = lo + ((hi - lo) // 2) # left mid
            hours_taken = calculate_hours(speed)

            if hours_taken <= h:
                hi = speed
            else:
                lo = speed + 1

        return lo


