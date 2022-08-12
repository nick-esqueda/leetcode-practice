class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        tab = [None] * (n + 1)
        tab[0], tab[1], tab[2] = 0, 1, 1
        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2] + tab[i - 3]
            
        return tab[n]
        
        