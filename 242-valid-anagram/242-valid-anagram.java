class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        Map<Character, Integer> sCounts = new HashMap<>();
        Map<Character, Integer> tCounts = new HashMap<>();
        
        for (int i = 0; i < s.length(); ++i) {
            char sChar = s.charAt(i), tChar = t.charAt(i);
            
            if (sCounts.containsKey(sChar)) {
                sCounts.replace(sChar, sCounts.get(sChar) + 1);
            } else {
                sCounts.put(sChar, 1);
            }
            
            if (tCounts.containsKey(tChar)) {
                tCounts.replace(tChar, tCounts.get(tChar) + 1);
            } else {
                tCounts.put(tChar, 1);
            }
        }
        
        return sCounts.equals(tCounts);
    }
}