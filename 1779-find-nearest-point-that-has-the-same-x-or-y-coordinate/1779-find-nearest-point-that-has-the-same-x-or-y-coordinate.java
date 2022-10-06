class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        /*
            valid points are only those that have either the same x or y coord.
            want the index of the valid point that is closest.
            iterate through points,
            compare the manhattan dist to the best dist so far,
            if it is strictly less than that dist, replace,
            return -1 if no valid points
        */
        
        int minDist = Integer.MAX_VALUE;
        int minIdx = 0;
        for (int i = 0; i < points.length; ++i) {
            int x2=points[i][0], y2=points[i][1];
            if ((x2 != x) && (y2 != y)) continue;
            
            int dist = Math.abs(x - x2) + Math.abs(y - y2);
            
            if (dist < minDist) {
                minIdx = i;
                minDist = dist;
            }
        }
        
        return minDist != Integer.MAX_VALUE ? minIdx : -1;
    }
}