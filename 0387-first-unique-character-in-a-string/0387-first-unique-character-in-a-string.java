class Solution {
    public int firstUniqChar(String s) {
        return hashMap(s);
    }
    
    public int hashMap(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (Character c : s.toCharArray()) {
            int charCount = counts.getOrDefault(c, 0);
            counts.put(c, charCount + 1);
        }
        
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            int count = counts.get(c);
            
            if (count == 1) {
                return i;
            }
        }
        
        return -1;
    }
}