class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        safe nodes are nodes that are not involved in any cycle
        need to know which nodes, when dfs'd on, were able to exit properly without any cycle encounters
        only nodes in the 'done' set will be the nodes that are safe
        """
        def is_safe(node, path):
            if node in done:
                return True
            if node in path:
                return False

            path.add(node)
            for nei in graph[node]:
                if not is_safe(nei, path):
                    return False
            path.remove(node)
            done.add(node)
            return True
        
        done = set()
        safe = []
        for node in range(len(graph)):
            if is_safe(node, set()) is True:
                safe.append(node)
        return safe