class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        as you traverse, if you deleted the edge that you just came along, then you won't get cycles
        choose the airport with a lower lexical value
        
        can't really for loop through the adjlist array, since the size of it will change every iteration...
        but, you could just iterate until that array is empty and pop off every time and visit that nei
        """
        graph = self.build_graph(tickets)
        itin = ["JFK"]
        def dft(node):
            if len(itin) == len(tickets) + 1:
                return True
            if node not in graph:
                return False
            
            copy = list(graph[node])
            for nei in copy:
                graph[node].pop(0)
                itin.append(nei)
                if dft(nei):
                    return True
                graph[node].append(nei)
                itin.pop()
        
        dft("JFK")
        return itin
        
    def build_graph(self, edges):
        graph = defaultdict(list)
        edges.sort()
        for a, b in edges:
            graph[a].append(b)
        return graph