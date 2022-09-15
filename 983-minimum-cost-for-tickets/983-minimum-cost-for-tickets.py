class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        days is an array that has the days of the year that you want to travel on.
        costs has the prices for a 1 day pass, 7 day pass, and a 30 day pass, respectively.
        each pass lets you travel for that many days (all inclusive)
        
        need the min cost to travel on every desired travel day.
        
        some days will be best to buy 1 day pass, if you don't want to travel for another 30 days or something.
        sometimes it might be better to buy a seven day pass, because you'll want to travel a few times within those 7 days, and buying 1 day passes would be more expensive.
        
        
        [1,4,6,7,8,20]
        [2,7,15]
         1 7 30
         
        [1,2,3,9]
        [2,7,15]
         1 7 30
         
        DP, see all possible options
        can decide to buy a 1 day ticket, 7, etc., and see what the cost is if you do each 
        
        need to know how long your pass let's you travel as you recurse downwards
        i.e. if you bought a 7 day pass and recurse downards, you should know when that pass runs out/expires.
        you could kind of skip to a certain day if you knew the indices
        or if you add the day pass to the current day, you'll get the day that it expires on. that way, you won't have to add to the cost until the new day exceeds that final day
        """
        pass_lens = [1, 7, 30]
        
        memo = {}
        def find_min(i, start_paying):
            key = (i, start_paying)
            if key in memo:
                return memo[key]
            if i >= len(days):
                return 0
            
            curr_day = days[i]
            
            min_cost = float('inf')
            for j in range(len(costs)):
                cost = 0
                if curr_day >= start_paying:
                    cost += costs[j]
                    cost += find_min(i + 1, curr_day + pass_lens[j])
                else:
                    cost += find_min(i + 1, start_paying)
                min_cost = min(min_cost, cost)
            
            memo[key] = min_cost
            return memo[key]
                
        return find_min(0, 0)