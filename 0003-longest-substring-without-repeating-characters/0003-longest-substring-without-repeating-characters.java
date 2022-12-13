class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> windowChars = new HashSet<>();
        int start = 0;
        int longest = 0;
        
        for (int end = 0; end < s.length(); ++end) {
            char c = s.charAt(end);

            if (windowChars.contains(c)) {
                // move start up to 1 after the first appearance of that letter.
                while (windowChars.contains(c)) {
                    char lChar = s.charAt(start);
                    windowChars.remove(lChar);
                    start += 1;
                }
            }

            windowChars.add(c); 
            longest = Math.max(longest, end - start + 1);
        }
        
        return longest;
    }
}