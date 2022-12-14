class Solution {
    public int[] plusOne(int[] digits) {
        /*
        what to do with 9's? have to carry 1 over.
        
        start from the back, and determine if there is a carry-over. (if 9, then true)
        while there's a carry-over, move back one and add 1, seeing if there is still a carry-over.
        repeat until carry-over is false.
        
        what if the carry over goes all the way? will need a new space at the beginning for the 1.
        */
        
        // return whileLoop(digits);
        // return forLoop(digits);
        return refactor(digits);
    }
    
    private int[] refactor(int[] digits) {
        // set all nines that you comes across to 0.
        // once you come across a non-nine, add 1 to it and return out.
        // if you make it out of the loop without finding a non-nine,
        // add a 1 to the beginning of the array and return that.
        
        for (int i = digits.length - 1; i >= 0; --i) {
            if (digits[i] != 9) {
                ++digits[i];
                return digits;
            }
            
            digits[i] = 0;
        }
        
        int[] newDigits = new int[digits.length + 1];
        newDigits[0] = 1;
        return newDigits;
    }
    
    private int[] forLoop(int[] digits) {
        for (int i = digits.length - 1; i >= 0; --i) {
            ++digits[i];
            if (digits[i] == 10) {
                digits[i] = 0;
            } else {
                break;
            }
        }
        
        // if you break out and you still have a carry over, need a new array with 1 at the front.
        return digits[0] == 0 ? bigCarry(digits) : digits;
    }
    
    private int[] whileLoop(int[] digits) {
        boolean carry = true;
        int i = digits.length - 1;
        while (i >= 0 && carry) {
            carry = false;
            
            ++digits[i];
            if (digits[i] == 10) {
                digits[i] = 0;
                carry = true;
            }
            
            --i;
        }
        
        return carry ? bigCarry(digits) : digits;
    }
    
    private int[] bigCarry(int[] digits) {
        int[] newDigits = new int[digits.length + 1];
        newDigits[0] = 1;
        for (int i = 0; i < digits.length; ++i) {
            newDigits[i + 1] = digits[i];
        }

        return newDigits;
    }
}