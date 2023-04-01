class Solution {
    public int titleToNumber(String columnTitle) {
        // each position in the string is another "place" in a base 26 number.
        // need to map each letter to a value 1-26.
        // iterate through the string, calculating the decimal value for each base 26 number,
        // and the add each to a running total.
        
        // 26^pos * (number in that position)
        // with this formula, you can iterate forwards and calculate the value for each position, while adding to a running total.
        
        
        // calculate the decimal value for each position and add to a running total.
        int sum = 0;
        int placePosition = columnTitle.length() - 1;
        for (char c : columnTitle.toCharArray()) {
            int value = (c - 64);
            double totalplacePositionitionValue = Math.pow(26, placePosition) * value;
            sum += (int) totalplacePositionitionValue;
            
            placePosition -= 1;
        }
        
        return sum;
    }
}