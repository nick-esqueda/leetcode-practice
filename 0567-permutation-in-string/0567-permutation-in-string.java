class Solution {
    public boolean checkInclusion(String s1, String s2) {
        /*
            create map of s1 char counts
            iterate down the length of s2, with a window of size s1.length
            use a map to hold the substr char counts
            each time you iterate, add the new letter and remove the old
            compare the maps on each iteration
            if both maps have the same contents, then you can just return out true
            if the R pointer leaves the end of s2, return false
            
        */
        
        if (s1.length() > s2.length()) return false;
        
        Map<Character, Integer> s1map = makeMap(s1, 0, s1.length() - 1);
        
        int i = 0;
        int j = s1.length() - 1;
        while (j < s2.length()) {
            Map<Character, Integer> substrMap = makeMap(s2, i, j);
            
            if (substrMap.equals(s1map)) return true;
            
            i += 1;
            j += 1;
        }
        
        return false;
    }
    
    public Map<Character, Integer> makeMap(String s, int start, int end) {
        Map<Character, Integer> res = new HashMap<>();
        
        for (int i = start; i <= end; ++i) {
            char c = s.charAt(i);
            if (!res.containsKey(c)) res.put(c, 0);
            res.put(c, res.get(c) + 1);
        }
        
        return res;
    }
    

    
}