class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        /*
            swap -> swapping two indices within the same string
            doesn't matter which string you choose to perform the swap.
            return true if you can make the strings equal by performing one swap (or none).
            
            exactly 2 unmatches (or 0)
            those unmatches have to have the same letters.
        */
        
        int diff1 = -1;
        int diff2 = -1;
        
        for (int i = 0; i < s1.length(); ++i) {
            char c1=s1.charAt(i), c2=s2.charAt(i);
            if (c1 == c2) continue;

            if (diff1 == -1) diff1 = i;
            else if (diff2 == -1) diff2 = i;
            else return false; // more than 2 differences
        }
        
        if (diff1 == -1 && diff2 == -1) return true;
        if (diff1 == -1 || diff2 == -1) return false;
        
        // at this point, you will have the indices where each difference occurs.
        // if the char in one string and one diff match the other char in the other diff
        // and vice versa, everything is good.
        return (s1.charAt(diff1) == s2.charAt(diff2)) && (s2.charAt(diff1) == s1.charAt(diff2));
    }
}