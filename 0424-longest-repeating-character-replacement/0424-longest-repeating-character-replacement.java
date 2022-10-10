class Solution {
    public int characterReplacement(String s, int k) {
        return twoPointer(s, k);
    }
    
    public int twoPointer(String s, int k) {       
        int maxLen = 0;
        int L = 0;
        Map<Character, Integer> counts = new HashMap<>();
        
        for (int R = 0; R < s.length(); ++R) {
            // put new char in the map.
            char newChar = s.charAt(R);
            if (counts.containsKey(newChar)) {
                counts.replace(newChar, counts.get(newChar) + 1);
            } else {
                counts.put(newChar, 1);
            }
            
            // make sure that substr is valid.
            // substr length - max char count
            while (((R - L + 1) - Collections.max(counts.values())) > k) {
                char lChar = s.charAt(L);
                counts.replace(lChar, counts.get(lChar) - 1);
                L += 1;
            }
            
            maxLen = Math.max(maxLen, R - L + 1);
        }                
        
        return maxLen;
    }
}