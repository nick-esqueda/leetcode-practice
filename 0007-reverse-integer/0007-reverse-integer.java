class Solution {
    public int reverse(int x) {
        boolean negative = x < 0;
        x = Math.abs(x);
        
        int overflowCheck = 0;
        int output = 0;
        
        while (x != 0) {
            int nextDigit = x % 10;
            
            // have to detect that we're about to overflow the int.
            overflowCheck = output;
            output = (output * 10) + nextDigit;
            if ((output - nextDigit) / 10 != overflowCheck) {
                return 0;
            } 
            
            x /= 10;
        }
        
        return negative ? -output : output;
    }
}