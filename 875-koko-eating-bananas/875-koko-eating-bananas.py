class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        the max of piles gets you the max k value 
        in other words, if koko eats max(piles) / hour, she'll go through each pile once per hour, meaning k == len(piles)
        but you don't want max, you want min
        
        
        koko can eat fast or slow (k) bananas/hr
        you want to find the slowest ban/hr value
        the max ban/hr value is always going to be the max of piles (max(piles))
        
        brute force:
        you can try a k of 1 and try to go through each pile to see if you can get to the end
            if not, you'll increment k and run through the whole array again
        to do this, you divide piles[i] by k (ceil) to get the number of hours it would take to finish that pile
        then you subtract that from 'h' and move on to the next pile and do the same
        if you get to the end of the array and the amount of hours taken == h, that k value is correct
        
        [1 ... 11] using this k value, how many hours does it take to eat all bananas?
        [3, 6, 7, 11] target = 8
        
        if you get an hours value greater than target (h)
            you need to eat more bananas/hr
            move lo up to mid + 1
        if you get an hours value less than target:
            you can eat less ban/hr
            move hi down to mid - 1
            
        PLAN:
        make an inner func that will... [get_hours]
            loop through the piles array
                divide piles[i] by k (ceiling) to get an hour amount that it takes to eat all those banas
                add that count to a running hour count
            return the hour count at end
            
        make an integer array from 1 up to max(piles)
        bin search through the integer array
        you will use each integer as the k value
        find the mid of the integer array, and throw it into the get_hours func
        if get_hours returns something greater than h:
            move lo up to mid + 1
        if get_hours returns something less than h:
            move hi down to mid - 1
        if get_hours == h, return that k value
        """
        
        def get_hours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        
        rtn = max(piles)
        lo, hi = 1, max(piles)
        while lo <= hi:
            k = (lo + hi) // 2
            hours = get_hours(k)
            
            if hours > h:
                lo = k + 1
            elif hours <= h:
                rtn = min(rtn, k)
                hi = k - 1
            
        return rtn
        