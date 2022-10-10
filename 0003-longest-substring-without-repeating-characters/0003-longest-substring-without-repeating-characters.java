class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        int L = 0;
        Set<Character> substr = new HashSet<>();
        
        for (int R = 0; R < s.length(); ++R) {
            char newChar = s.charAt(R);
            
            // move L until the dup is out of substr.
            while (substr.contains(newChar)) {
                substr.remove(s.charAt(L));
                L += 1;
            }
            
            substr.add(newChar);
            maxLen = Math.max(maxLen, (R - L) + 1);
        }
        
        return maxLen;
    }
}