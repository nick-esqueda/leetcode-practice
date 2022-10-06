class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        // return sorting(arr);
        return math(arr);
    }
        
    public boolean math(int[] arr) {
        /*
            with the max and min of arr, you can predict what size the arith prog would be.
                > (max - min) / (arr.length - 1) (-1 because we want the differences/edges between)
            with that diff, you can simulate what values would be the proper arith prog.
            put the nums in the arr in a set,
            loop through what the arith prog should be,
            if the curr num is not in the set, then that num doesn't belong.
            return true at end if you made it through the prog.
            
            edge cases: 
            is there a possibility (max-min)/(length - 1) (arith prog diff) will be a decimal?
                > no, because if it was a decimal, then some nums in the arr would also be.
                > this is an indicator that the prog is not possible, period.
        */
        
        int min=Integer.MAX_VALUE, max=Integer.MIN_VALUE;
        Set<Integer> arrNums = new HashSet<>();
        for (int num: arr) {
            min = Math.min(min, num);
            max = Math.max(max, num);
            arrNums.add(num);
        }
        
        // return false if an arith prog is not possible with integers. (doesn't divide evenly)
        if ((max - min) % (arr.length - 1) != 0) return false;
        
        int arithDiff = (max - min) / (arr.length - 1);
        
        // iterate through the proper prog, and check set to see if matches.
        // for (int i = min; i <= max; i += arithDiff) { // this will not work when min == max
        //     if (!(arrNums.contains(i))) return false;
        // }
        
        int i = 0;
        while (i < arr.length) {
            // start at min, and work your way up the progression with min.
            if (!(arrNums.contains(min))) return false;
            min += arithDiff;
            ++i;
        }
        
        return true;
    }
        
    public boolean sorting(int[] arr) {
        /*
            artith prog - difference between two adjacent elements are the same.
                ex. 2, 4, 6 -> all have diff of 2
            return true if arr can be rearranged to be an arith prog.
            sort the arr so that the possible arith prog can be checked.
        */
        
        Arrays.sort(arr);
        
        int diff = arr[1] - arr[0];
        for (int i = 0; i < arr.length - 1; ++i) {
            if (arr[i + 1] - arr[i] != diff) return false;
        }
        
        return true;
    }
}