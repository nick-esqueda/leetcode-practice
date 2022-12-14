class Solution {
    public int mySqrt(int x) {
        // the square root is the inverse of the square.
        // square - this number multiplied by itself x times.
        // square root - x number multiplied by itself 2 times.
        // square root - what number multiplied by itself 2 times gets this number?
        
        // can iterate through all squares and find the last one underneath that number?
        
        long num = 1;
        while (num * num <= x) {
            ++num;
        }
        
        return (int) num - 1;
    }
}