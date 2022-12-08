class Solution {
    public void wallsAndGates(int[][] rooms) {
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < rooms.length; ++r) {
            for (int c = 0; c < rooms[0].length; ++c) {
                if (rooms[r][c] == 0) {
                    q.offer(new int[] { r, c });
                }
            }
        }
        
        int dist = -1;
        while (!q.isEmpty()) {
            dist += 1;
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                int[] pos = q.poll();
                int r = pos[0], c = pos[1];
                
                if (rooms[r][c] == Integer.MAX_VALUE) {
                    rooms[r][c] = dist;
                }
                
                List<int[]> neighbors = getNeighbors(r, c, rooms);
                for (int[] nei : neighbors) {
                    q.offer(nei);
                }
            }
        }
    }
    
    public List<int[]> getNeighbors(int r, int c, int[][] rooms) {
        List<int[]> neis = new ArrayList<>();
        neis.add(new int[] { r - 1, c });
        neis.add(new int[] { r + 1, c });
        neis.add(new int[] { r, c - 1 });
        neis.add(new int[] { r, c + 1 });
        
        List<int[]> finalNeis = new ArrayList<>();
        for (int[] nei : neis) {
            int nR = nei[0], nC = nei[1];
            if (nR >= 0 && nR < rooms.length &&
                nC >= 0 && nC < rooms[0].length &&
                rooms[nR][nC] == Integer.MAX_VALUE) {
                finalNeis.add(nei);
            }
        }
        
        return finalNeis;
    }
    
    public void printGraph(int[][] graph) {
        for (int[] row : graph) {
            System.out.println(Arrays.toString(row));
        }
        System.out.println();
    }
}