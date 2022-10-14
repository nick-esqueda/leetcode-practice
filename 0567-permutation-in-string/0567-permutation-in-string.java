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
        
        int[] s1Counts = new int[26];
        for (char c : s1.toCharArray()) s1Counts[c - 'a']++;
        
        int i = 0;
        int j = s1.length() - 1;
        while (j < s2.length()) {
            int[] substrCounts = makeMap(s2, i, j);
            
            if (isEqual(s1Counts, substrCounts)) return true;
            
            i += 1;
            j += 1;
        }
        
        return false;
    }
    
    public int[] makeMap(String s, int start, int end) {
        int[] s2Counts = new int[26];
        
        for (int i = start; i <= end; ++i) {
            char c = s.charAt(i);
            s2Counts[c - 'a']++;
        }
        
        return s2Counts;
    }
    
    public boolean isEqual(int[] a, int[] b) {
        for (int i = 0; i < a.length; ++i) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }

    
}