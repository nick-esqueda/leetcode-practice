class Solution {
    public int largestPerimeter(int[] nums) {
        /*
            the sum of the lengths of the 2 smaller sides must be greater than the biggest side.
            the array contains many lengths, and you want to use the the biggest 3 possible to 
            make the triangle.
            sort the array to have immediate access to the biggest lengths, and move through the 
            array one by one until you find a valid triangle.
        */
        
        List<Integer> list = new ArrayList<>();
        for (int num : nums) list.add(num);
        
        Collections.sort(list);
        Collections.reverse(list);
        
        System.out.println(list);
        
        for (int i = 0; i < list.size() - 2; ++i) {
            if (list.get(i + 1) + list.get(i + 2) > list.get(i))
                return list.get(i) + list.get(i + 1) + list.get(i + 2);
        }
        
        return 0;
    }
}