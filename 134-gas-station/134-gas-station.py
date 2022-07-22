class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas[prices of gas] -> [1, 2, 3, 4, 5] <- ! will be returning one of these indices
        cost[amount of gas that'll burn to go to the next station] -> [3, 4, 5, 1, 2]
        
        tank = 0 + 4 = 4 - 1 + 5 = 8 - 2 + 1 = 7 - 3 + 2 = 6 - 4 + 3 = 5 - 5 + 4 = 4
        g[1, 2, 3, 4, 5]
                   i                                  
        c[3, 4, 5, 1, 2]
        
         [(1,-1),  ,  ,  ,  ,]
        
        tank = 0 + 4 = (4 - 3) + 2 = (3 - 3) + 3 = (3 - 4) x
        g[2, 3, 4]
                i        
        c[3, 4, 3]
        
        
        if the tank ever goes negative, you can't start at that position
        
        start the traversal at every index
        if the traversal comes back as -1, save that to a memo/tab
        
        """
        if sum(gas) < sum(cost):
            return -1
        
        diff = [gas - cost for gas, cost in zip(gas, cost)]
        
        tank = 0
        start = 0
        for i in range(len(diff)):
            tank += diff[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start
