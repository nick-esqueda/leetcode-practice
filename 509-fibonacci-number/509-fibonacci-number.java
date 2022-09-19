class Solution {
    public int fib(int n) {
        if (n <= 1) return n;
    
        int[] tab = new int[n + 1];
        tab[0] = 0;
        tab[1] = 1;
        
        for (int i = 2; i <= n; ++i)
            tab[i] = tab[i - 1] + tab[i - 2];
        
        return tab[tab.length - 1];
    }
}