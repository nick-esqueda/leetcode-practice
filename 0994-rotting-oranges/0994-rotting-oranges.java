class Solution {
    public int orangesRotting(int[][] grid) {
        List<int[]> rottingOranges = getRottenOranges(grid);

        int count = 0;
        Deque<int[]> q = new ArrayDeque<>();
        for (int[] orange : rottingOranges) q.offer(orange);

        while (!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                int[] pos = q.poll();

                List<int[]> neighbors = getNeighbors(pos, grid);
                for (int[] nei : neighbors) {
                    q.offer(nei);
                }
            }
                
            if (q.size() == 0) break;
            count += 1;
        }

        return freshExists(grid) ? -1 : count;
    }

    private List<int[]> getNeighbors(int[] pos, int[][] grid) {
        // consider only fresh oranges valid.
        // turn those to rotten in matrix before returning. 
        int r = pos[0], c = pos[1];
        List<int[]> neighbors = new ArrayList<>();

        if (r - 1 >= 0 && grid[r - 1][c] == 1) {
            grid[r - 1][c] = 2;
            neighbors.add(new int[] { r - 1, c });
        }

        if (r + 1 < grid.length && grid[r + 1][c] == 1) {
            grid[r + 1][c] = 2;
            neighbors.add(new int[] { r + 1, c });
        }

        if (c - 1 >= 0 && grid[r][c - 1] == 1) {
            neighbors.add(new int[] { r, c - 1 });
            grid[r][c - 1] = 2;
        }

        if (c + 1 < grid[0].length && grid[r][c + 1] == 1) {
            grid[r][c + 1] = 2;
            neighbors.add(new int[] { r, c + 1 });
        }

        return neighbors;
    }

    private boolean freshExists(int[][] grid) {
        for (int r = 0; r < grid.length; ++r) {
            for (int c = 0; c < grid[0].length; ++c) {
                if (grid[r][c] == 1) return true;
            }
        }

        return false;
    }

    private List<int[]> getRottenOranges(int[][] grid) {
        List<int[]> rotting = new ArrayList<>();
        for (int r = 0; r < grid.length; ++r) {
            for (int c = 0; c < grid[0].length; ++c) {
                if (grid[r][c] == 2) {
                    rotting.add(new int[] { r, c });
                }
            }
        }

        return rotting;
    }
}