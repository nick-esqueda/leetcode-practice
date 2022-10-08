class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /*
            make freq map.
            
            for k amount of times:
                find the max count/key (loop),
                put the number assoc'd with that count in the result,
                delete that key from the map.
        */
        
        // { num: freq, ... }
        Map<Integer, Integer> counts = new HashMap<>(); 
        
        for (int num: nums) {
            if (counts.containsKey(num)) {
                counts.replace(num, counts.get(num) + 1);
            } else {
                counts.put(num, 1);
            }
        }
        
        int[] topK = new int[k];
        while (k > 0) {
            int maxNum = Integer.MAX_VALUE;
            for (int num: counts.keySet()) {
                if (maxNum == Integer.MAX_VALUE) maxNum = num; // initialize var.
                if (counts.get(num) > counts.get(maxNum)) {
                    maxNum = num;
                }
            }
            
            topK[k - 1] = maxNum;
            counts.remove(maxNum);
            k--;
        }
        
        return topK;
    }
}