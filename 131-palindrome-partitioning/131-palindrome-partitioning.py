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
        
        def get_partitions(string):
            if len(string) == 0:
                all_partitions.append(partition[::])
                return
            
            for i in range(len(string)):
                substr = string[0:i + 1]
                if is_palin(substr):
                    partition.append(substr)
                    get_partitions(string[i + 1:])
                    partition.pop()
            
        get_partitions(s)
        return all_partitions
        