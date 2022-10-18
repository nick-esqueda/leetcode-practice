class Solution {
    public boolean isHappy(int n) {
        /*
            this process won't continue until infinity, since the square of 9 (largest digit) added to itself can only go so high.
            the largest "next num" you can get with 'x' amount of digits is the "next num" of all 9's.
            any lesser digits will just provide a lesser sum.
            9999 -> 324
            999 -> 243
            99 -> 162
            9 -> 81
            
            if you come across a num that has already been "seen", the process will repeat infinitely.
            2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -|> 4...
            
            detect if there is a cycle in the process.
        */
        
        // return set(n);
        return floyds(n);
    }
    
    public boolean floyds(int n) {
        // set slow and fast on two different "nodes" to allow first iteration of while loop.
        int slow = n;
        int fast = getNext(n);
        
        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        
        return fast == 1;
    }
    
    public int getNext(int n) {
        int sum = 0;
        while (n != 0) {
            int digit = n % 10;
            sum += Math.pow(digit, 2);
            n /= 10;
        }
        
        return sum;
    }
    
    public boolean set(int n) {
        Set<Integer> seen = new HashSet<>();
        
        while (n != 1) {
            if (seen.contains(n)) return false;
            seen.add(n);
            
            n = sumDigitSquares(n);
        }
        
        return true;
    }
    
    public int sumDigitSquares(int n) {
        int digitSum = 0;
        while (n != 0) {
            int digit = n % 10;
            digitSum += Math.pow(digit, 2);
            n /= 10;
        }
        
        return digitSum;
    }
}