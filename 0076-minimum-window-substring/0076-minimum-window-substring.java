class Solution {
    public String minWindow(String s, String t) {
        /*
            want the substring of S of the smallest length that has every char in T in it.
            
            expand window until the window has all T chars.
            once you have a match:
                contract window until about to go into deficit (L char count in window == L char count in tMap)
                    - this is to "optimize" the string length before comparisons
                compare and swap min.
                remove L char from window and move it up 1
            loop again.
                    
            tMap =   { A: 1, B: 1, C: 1 }
            window = { A: 1, B: 1, C: 1 }
            minLen = 6
            
            A A D O B E C O D E B A N C
            L
                        R
                        
        */
        
        if (t.length() > s.length()) return "";
        
        // construct map of T chars and initialize window map.
        Map<Character, Integer> tMap = new HashMap<>();
        Map<Character, Integer> windowMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            if (!tMap.containsKey(c)) tMap.put(c, 0);
            if (!windowMap.containsKey(c)) windowMap.put(c, 0);
            tMap.replace(c, tMap.get(c) + 1);
        }
        
        int i = 0;
        int j = s.length(); // purposefully OOB for min value logic.
        int L = 0;
        for (int R = 0; R < s.length(); ++R) { // window logic.
            char rChar = s.charAt(R);
            
            // move on if r char is irrelevant.
            if (!tMap.containsKey(rChar)) continue;
            
            // +1 in window if r char is relevant.
            windowMap.replace(rChar, windowMap.get(rChar) + 1);
            
            // if the window has all necessary chars...
            if (windowIsValid(tMap, windowMap)) {
                // move L up to trim out unnecessary chars.
                while (true) {
                    char lChar = s.charAt(L);
                    if (tMap.containsKey(lChar)) {
                        if (windowMap.get(lChar) <= tMap.get(lChar)) break;
                        windowMap.replace(lChar, windowMap.get(lChar) - 1);
                    }
                    L += 1;
                }

                // compare and swap.
                if (((R - L + 1) < (j - i + 1))) {
                    i = L;
                    j = R;
                }
                
                // move L up by one to begin the search for a new valid window.
                windowMap.replace(s.charAt(L), windowMap.get(s.charAt(L)) - 1);
                L += 1;
            }
        }
        
        return j == s.length() ? "" : s.substring(i, j + 1);
    }
    
    public boolean windowIsValid(Map<Character, Integer> tMap, Map<Character, Integer> windowMap) {
        for (char c : tMap.keySet()) {
            if (windowMap.get(c) < tMap.get(c)) return false;
        }
        return true;
    }
}