class Solution {
    public int mySqrt(int x) {
        // return bruteForce(x);
        return binarySearch(x);
    }
    
    private int binarySearch(int x) {
        // acceptable vals are <= x
        // unacceptable vals are > x.
        long lo = 0; 
        long hi = x;
        
        while (lo < hi) {
            long num = lo + ((hi - lo + 1) / 2); // right mid.
            long square = num * num;

            if (square <= x) {
                lo = num;
            } else {
                hi = num - 1;
            }
        }
        
        return (int) lo;
    }    
    
    private int bruteForce(int x) {
        long num = 1;
        while (num * num <= x) {
            ++num;
        }
        
        return (int) num - 1;
        
        // THOUGHTS:
        // the square root is the inverse of the square.
        // square - this number multiplied by itself x times.
        // square root - x number multiplied by itself 2 times.
        // square root - what number multiplied by itself 2 times gets this number?
        
        // can iterate through all squares and find the last one underneath that number?
    }
}