class Solution {
    public int lengthOfLongestSubstring(String s) {
        // return set(s);
        return map(s);
    }
    
    private int map(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int startIdx = 0;
        int longest = 0;
        
        for (int endIdx = 0; endIdx < s.length(); ++endIdx) {
            char currChar = s.charAt(endIdx);
            if (lastSeen.containsKey(currChar) && lastSeen.get(currChar) >= startIdx) {
                startIdx = lastSeen.get(currChar) + 1;
            }
            
            longest = Math.max(longest, endIdx - startIdx + 1);
            lastSeen.put(currChar, endIdx);
        }
        
        return longest;
    }
    
    private int set(String s) {
        Set<Character> windowChars = new HashSet<>();
        int start = 0;
        int longest = 0;
        
        for (int end = 0; end < s.length(); ++end) {
            char c = s.charAt(end);

            // move start up to 1 after the first appearance of that letter.
            while (windowChars.contains(c)) {
                char lChar = s.charAt(start);
                windowChars.remove(lChar);
                start += 1;
            }

            windowChars.add(c); 
            longest = Math.max(longest, end - start + 1);
        }
        
        return longest;
    }
}