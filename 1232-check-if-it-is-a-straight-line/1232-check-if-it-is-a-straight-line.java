class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        /*
            the diff between the first 2 x coords and first 2 y coords
            will give you the slope of the line of the first two points.
            this slope should remain the same throughout the loop.
            
            edge cases:
            dividing by 0 - with the normal slope equation, you might end up
            dividing by 0. to avoid that, the slope checking equation can be
            rewritten with multiplication:
                (x2 - x1) / (y2 - y1) == (x3 - x2) / (y3 - y2)
                (x2 - x1) * (y3 - y2) == (y2 - y1) * (x3 - x2)
        */
        
        int x1 = coordinates[0][0], x2 = coordinates[1][0],
            y1 = coordinates[0][1], y2 = coordinates[1][1];
        
        for (int i = 2; i < coordinates.length; ++i) {
            int[] coord = coordinates[i];
            int x3 = coord[0], y3 = coord[1];
            
            if ((x2 - x1) * (y3 - y2) != (y2 - y1) * (x3 - x2))
                return false;
        }
        
        return true;
    }
}