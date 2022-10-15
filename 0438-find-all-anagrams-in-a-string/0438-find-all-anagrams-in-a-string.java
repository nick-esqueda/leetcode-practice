class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] pCounts = new int[26];
        for (int i = 0; i < p.length(); ++i) {
            pCounts[p.charAt(i) - 'a']++;
        }
        
        List<Integer> res = new ArrayList<>();
        int[] sCounts = new int[26];
        
        for (int R = 0; R < s.length(); ++R) {
            sCounts[s.charAt(R) - 'a']++;
            
            int oldL = R - p.length();
            if (oldL >= 0) sCounts[s.charAt(oldL) - 'a']--;
            
            if (Arrays.equals(pCounts, sCounts)) res.add(oldL + 1);
        }
        
        return res;
    }
}