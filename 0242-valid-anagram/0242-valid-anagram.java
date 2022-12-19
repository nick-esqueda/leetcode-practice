class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] diff = new int[26];
        
        for (int i = 0; i < s.length(); ++i) {
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            
            ++diff[sChar - 'a'];
            --diff[tChar - 'a'];
        }
        
        for (int i = 0; i < diff.length; ++i) {
            if (diff[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
}