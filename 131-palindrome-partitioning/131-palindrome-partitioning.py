class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        can choose to take a substr starting at each index
        if the substr is a palindrome, add that to the cur partition, then recurse with the rest of the str
        """
        all_partitions = []
        partition = []
        
        def is_palin(string):
            return string == string[::-1]
        
        def get_partitions(i):
            if i >= len(s):
                all_partitions.append(partition[::])
                return
            
            for j in range(i, len(s)):
                substr = s[i:j + 1]
                if is_palin(substr):
                    partition.append(substr)
                    get_partitions(j + 1)
                    partition.pop()
            
        get_partitions(0)
        return all_partitions
        