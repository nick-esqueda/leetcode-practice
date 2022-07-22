class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        idk
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
