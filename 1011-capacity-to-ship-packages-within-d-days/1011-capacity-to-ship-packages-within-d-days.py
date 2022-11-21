class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculate_days(cap):
            days = 1
            cur_load = 0
            for weight in weights:
                if cur_load + weight > cap:
                    days += 1
                    cur_load = 0
                cur_load += weight
            return days

        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            cap = lo + ((hi - lo) // 2) # left mid
            d = calculate_days(cap)

            if d <= days:
                hi = cap
            else:
                lo = cap + 1

        return lo

        """ THOUGHT PROCESS ==============================
        PROBLEM:
        each num in list is a weight.
        every day, load the ship with as many packages from "weights" as can fit.
        you must load the packages in order of "weights".
        you can't exceed ship's weight capacity. (<= cap)
        find the least capacity of a ship that would allow all of the packages to be shipped in "days" days.

        THOUGHTS:
        you're wanting the FIND the least capacity of the ship. you're looking for the actual capacity
            - in other words, we don't know what ship that we want. we are doing this to find the optimal ship to use.

        you want to try and use up all of the days, because that means you can have a smaller ship/smaller capacity.

        we're searching for the minimum ship capacity.

        you're essentially asking, out of the "possible values" for this range of unknown values/not given values, what's the best?

        an example capacity could be the sum of all weights. that's because you need to store all of the packages,
        so you could just have 1 ship that can hold every single package. that means you would ship everything in just one day.

        but, of course, we want the MINIMUM capacity possible. that would be out maximum cap, clearly. 
        so, sum(weights) is the upper bound, and you want to look for a capacity (target) value lower than that.
        the lower bound has to be max(weights), because we can't load more weight than the ship's cap.

        now that we have a lower bound and an upper bound, we can start searching those values.
        on each step, we have to calculate how many "DAYS" we would take to ship with that capacity.
            - if we went too fast (d < D), then we want less capacity (want smaller cap values, move left in cap_vals)
            - if we want too slow (d > D), then we want a bigger capactiy (want higher cap values, move right in cap_vals)

        we know that we might not find a capacity that will give us exactly D days, but we will accept lower "days" values.
        this is how we know that this is an "optimal value"-style binary search problem.

        CAPACITY VALUES - the array that you're performing the search on. target is in here.
        DAYS - the calculation you make based on the capacity values that tell you where to look for target. this is the "guide".


        EXAMPLE:
        [1,2,3,4,5,6,7,8,9,10] d = 5 
         i

        min_cap = 10, max_cap = 55
        [10, ..., 55] <- possible capacity values.

        d = (calc from "weights" and "cap_val")

        """
        


















