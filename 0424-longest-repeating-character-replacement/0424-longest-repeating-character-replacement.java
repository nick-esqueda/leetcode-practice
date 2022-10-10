class Solution {
    public int characterReplacement(String s, int k) {
        return twoPointer(s, k);
    }
    
    public int twoPointer(String s, int k) {
        /*
            you have the length of the string...
            use map with char counts?
            you have the max char in the map, and the length...
            if you subtract (length of str - max map char), that should be <= k.
            the ratio of maxChar/len needs to stay the same (under k) to find the maxLen.
            
            after you add newChar to the map, check maxChar/len ratio.
            if ratio is > k, need to:
                move L up until the ratio is restored.
                ? just continue in the loop for this?
            
            { a: 2, b: 6 }
            A A B B B A B A B B B B     K=2
                i             j
            
            len = 8
        */
        
        int L = 0;
        Map<Character, Integer> counts = new HashMap<>();
        int maxLen = 0;
        
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