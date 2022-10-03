class Solution {
    public int countOdds(int low, int high) {
        /*
            both odd -> (high - low // 2) + 1
            one even -> (high - low // 2) + 1
            both even -> high - low // 2
            
            3, 7 -> 3
            
            3, 8 -> 3
            4, 9 -> 3
            
            10, 16 -> 3 -> hi - low // 2
        */
        int count = (high - low) / 2;
        
        if ((low & 1) == 0 && (high & 1) == 0) return count;
        else return count + 1;
    }
}