class Solution {
    public boolean isPalindrome(String s) {
        // return reverse(s);
        return twoPointer(s);
    }
    
    public boolean twoPointer(String s) {
        String str = s.toLowerCase();
        
        int l = 0;
        int r = str.length() - 1;
        while (l < r) {
            char lChar = str.charAt(l);
            char rChar = str.charAt(r);
            
            if (!Character.isLetterOrDigit(lChar)) {
                l += 1;
            } else if (!Character.isLetterOrDigit(rChar)) {
                r -= 1;
            } else {
                if (lChar != rChar) return false;
                l += 1;
                r -= 1;
            }
        }
        
        return true;
    }
    
    public boolean reverse(String s) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        
        String forward = sb.toString();
        String backward = sb.reverse().toString();
        
        return forward.equals(backward);
    }
}