public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        // if no strs, return a value to let decode() know.
        if (strs.size() == 0) return Character.toString((char) 258);
        
        StringBuilder sb = new StringBuilder();
        char delim = (char) 257;
        
        for (String str: strs) {
            sb.append(str);
            sb.append(delim);
        }
        
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        String delim = Character.toString((char) 258);
        // return empty list if original strs was empty.
        if (s.equals(delim)) return new ArrayList();
        
        delim = Character.toString((char) 257);
        String[] strs = s.split(delim, -1); // -1 will keep some whitespace.
        return Arrays.asList(strs);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));