class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        two pointers.
        need to remember which letters that you've come across.
        this will be tricky, because if one substr has repeating chars, it won't if you move L up by 1.
        the dup might actually come from somewhere in the middle though...
        
        keep a set to remember which chars are in substr.
        if R iterates forward and immediately finds a dup, then you have to:
            move L up until that L dup is no longer in the substr,
                (remove chars from set as move L up since no longer in substr)
            then you can keep looping.
        always take the length and compare to max.
            
        abcadef
         i j
         
        a h b c d b e f
        i         j
        */
        
        int L = 0;
        Set<Character> substr = new HashSet<>();
        int maxLen = 0;
        
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