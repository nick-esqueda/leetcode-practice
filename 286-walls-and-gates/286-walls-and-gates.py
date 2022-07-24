class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        vis = set(q)
        for r in range(len(rooms)):
            for c in range(len(rooms[r])):
                if rooms[r][c] == 0:
                    q.append((r, c, 0))
                    vis.add((r, c))
                    
        empty_room = 2**31 - 1
        while q:
            cur = q.popleft()
            r, c, d = cur
            
            rooms[r][c] = d
            
            neis = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neis:
                if (nr >= 0 and nr < len(rooms) and nc >= 0 and nc < len(rooms[r]) and
                    rooms[nr][nc] == empty_room and (nr, nc) not in vis):
                    q.append((nr, nc, d + 1))
                    vis.add((nr, nc))
                    
            
            
