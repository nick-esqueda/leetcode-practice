class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        bellman ford
        if instead of relaxing edges for v - 1 times, if you instead relax only k times....
            but, you could have the optimal iteration and find every distance in the first iteration, which would give you the shortest distance DISREGARDING k
        so to fix this, you should skip edges that wouldn't have been reachable yet if you were treating each iteration as a BFS layer
        treat each iteration of the outer loop as a BFS layer - don't expand edges that don't touch the src node at first, and so on
        to do this:
            use an array that you reference but not modify on every iteration
            modify a temp array with the updated costs that you find coming from the new node
            but to find those costs, reference the unmodified array
            this ensures that you can't expand nodes/edges that were just expanded in the same iteration
        """
        static_costs = [float('inf')] * n
        static_costs[src] = 0
        for _ in range(k + 1):
            updated = False
            temp = static_costs.copy()
            for cur, nei, wgt in flights:
                if static_costs[cur] + wgt < temp[nei]:
                    temp[nei] = static_costs[cur] + wgt
                    updated = True
            static_costs = temp
            if not updated:
                break
                
        return static_costs[dst] if static_costs[dst] != float('inf') else -1