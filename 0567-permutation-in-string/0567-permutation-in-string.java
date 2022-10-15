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
        int[] substrCounts = new int[26];
        for (char c : s1.toCharArray()) s1Counts[c - 'a']++;
        
        int L = 0;
        for (int R = 0; R < s2.length(); ++R) {
            substrCounts[s2.charAt(R) - 'a']++;
            if (isEqual(s1Counts, substrCounts)) return true; 

            if (R >= s1.length() - 1) { // only move L if R has caught up to s1.length.
                substrCounts[s2.charAt(L) - 'a']--;
                L += 1;
            }
        }
        
        return false;
    }
    
    public boolean isEqual(int[] a, int[] b) {
        for (int i = 0; i < a.length; ++i) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }

    
}