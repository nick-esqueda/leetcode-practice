class Solution {
    public boolean isAnagram(String s, String t) {
        return sorting(s, t);
        // return mapCounter(s, t);
        // return arrayCounter(s, t);
    }
    
    public boolean arrayCounter(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] sCounts = new int[26];
        int[] tCounts = new int[26];
        
        for (int i = 0; i < s.length(); ++i) {
            sCounts[s.charAt(i) - 'a']++;
            tCounts[t.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i < sCounts.length; ++i) {
            if (sCounts[i] != tCounts[i]) return false;
        }
        
        return true;
    }
    
    public boolean mapCounter(String s, String t) {
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
    
    public boolean sorting(String s, String t) {
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        
        return Arrays.equals(sArr, tArr);
    }
}