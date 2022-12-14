class Solution {
    public int removeDuplicates(int[] nums) {
        // remove dups in place
        // each element should appear only once after all dups are replaced.
        // replace with what?
        // move the duplicates to the back of the array. (first 'k' ele.s should be the answer.)
        // no extra memory
        // need to return k as well as modify the array.
        
        /*
        if we could use a DS, then we could rememeber the index of dups, and then move them to the back.
            - or, remember the first occurrence of the num, then move those to the front...
            
        how to do this WITHOUT a nested for loop....?? bc without the DS, we can't really know if a new number is actually a duplicate or not. 
        
        AHH, array is in sorted order always!!!! not random numbers.
        this means that the very first instance of the number will be the unique one.
        so every number after that one might be a duplicate.
        
        in the loop...
        if the previous num == this one, the this one's gotta go to the back of the array.
        how to put in the back of the array?
        problem is, if you do an array swap, you'll destroy the ordering of the array...
        how to not destroy the order?
        what if you just moved on to the next number, and once you find it, move it back until the idx of the first occurence?
        
        
        "the next num goes here (i + 1). all others can just move back." <- this will let you do an array swap i think
        
        [0,1,2,3,0,2,1,3,1,4]
                 ^
                           s
                           
            
        lookingForLastOf = 7
        [1, 2, 4, 5, 6, 7, 4, 1, 2, 1, 7, 4]
                        ^
                                          s
        k will be the final index + 1 after the loop is done. (just update a counter instead)
        
        currNum = 1
        [1, 2, 1]
               k
                  f
        */
        
        int k = 0;
        int finalNumOccurrence = 0;
        while (finalNumOccurrence < nums.length) {
            int currNum = nums[finalNumOccurrence];
            while (finalNumOccurrence < nums.length - 1 && nums[finalNumOccurrence + 1] == currNum) {
                ++finalNumOccurrence;
            }
            
            swap(k++, finalNumOccurrence++, nums);
        }
        
        return k;
    }
    
    private void swap(int idxA, int idxB, int[] nums) {
        int temp = nums[idxA];
        nums[idxA] = nums[idxB];
        nums[idxB] = temp;
    }
}