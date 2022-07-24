class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        khan's algorithm
        can find the max of all times at each step and then add that max to a 'months' variable
        by the time you complete the bfs, months will have the max path sum / months needed to complete all courses
        no cycles
        """
        adj = { i: [] for i in range(1, n + 1) } # 1 -> n
        in_count = [0] * (n + 1) # courses are labeled 1 -> n, so you have an empty slot for index 0
        for prev, nxt in relations:
            adj[prev].append(nxt)
            in_count[nxt] += 1
            
        q = deque()
        dist = [0] * (n + 1)
        for cor in adj:
            if in_count[cor] == 0:
                q.append(cor)
                dist[cor] = time[cor - 1]
        
        while q:
            cor = q.popleft()
            for child in adj[cor]:
                dist[child] = max(dist[child], dist[cor] + time[child - 1])
                in_count[child] -= 1
                if in_count[child] == 0:
                    q.append(child)
            
        return max(dist)
