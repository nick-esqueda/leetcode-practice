class Solution {
    public void reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            swap(left, right, s);
            ++left;
            --right;
        }
    }
    
    private void swap(int idxA, int idxB, char[] s) {
        char temp = s[idxA];
        s[idxA] = s[idxB];
        s[idxB] = temp;
    }
}