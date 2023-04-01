class Solution {
    private  Map<Character, Integer> letterToValueMap = new HashMap<>();
    
    public int titleToNumber(String columnTitle) {
        // each position in the string is another "place" in a base 26 number.
        // need to map each letter to a value 1-26.
        // iterate through the string, calculating the decimal value for each base 26 number,
        // and the add each to a running total.
        
        // 26^pos * (number in that position)
        // with this formula, you can iterate forwards and calculate the value for each position, while adding to a running total.
        
        
        // populate the letter: value map.
        populateLetterToValueMap();
        
        // calculate the decimal value for each position and add to a running total.
        int sum = 0;
        int pos = columnTitle.length() - 1;
        for (int i = 0; i < columnTitle.length(); ++i) {
            int value = letterToValueMap.get(columnTitle.charAt(i));
            double totalPositionValue = Math.pow(26, pos) * value;
            sum += (int) totalPositionValue;
            pos -= 1;
        }
        
        return sum;
        
    }
    
    private void populateLetterToValueMap() {
        for (int i = 0; i < 26; ++i) {
            char c = (char) ('A' + i);
            letterToValueMap.put(c, i + 1);
        }
    }
}