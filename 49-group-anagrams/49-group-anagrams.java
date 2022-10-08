class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> groups = new HashMap<>();
        
        for (String s: strs) {
            // build the counts array to determine group.
            int[] counts = new int[26];
            for (char c: s.toCharArray()) {
                counts[c - 'a']++;
            }
            
            List<Integer> group = new ArrayList<>();
            for (int count: counts) group.add(count);
            
            // if that group exists, add this string to that group
            if (groups.containsKey(group)) groups.get(group).add(s);
            // if group doesn't exist, add the group and the string in a list
            else groups.put(group, new ArrayList<>(Arrays.asList(s)));
        }
        
        return new ArrayList<>(groups.values());
    }
}