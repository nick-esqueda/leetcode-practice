class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            char lC = s.charAt(l);
            char rC = s.charAt(r);
            
            if (!Character.isLetterOrDigit(lC)) {
                ++l;
                continue;
            }
            
            if (!Character.isLetterOrDigit(rC)) {
                --r;
                continue;
            }
            
            if (lC != rC) return false;
            
            ++l;
            --r;
        }
        
        return true;
    }
}