class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        in order to check if there is a num before curr num, use a set of nums for O(1) lookup
        
        if num - 1 is not in the set, this num is the start of a sequence, so.....?
        if num + 1 is not in the set, this num is the end of a sequence
        if num - 1 is in the set, this num is part of a sequence
        if num + 1 is in the set, this num is part of a sequence
        
        once you find the end of a seq:
            num = the end num of that seq
            seq_len = 1
            while num - 1 in set:
                seq_len += 1
        then reassign a max_seq variable accordingly
        """
        def get_seq_len(num):
            seq_len = 1
            while (num - 1) in num_set:
                seq_len += 1
                num -= 1
            return seq_len
        
        
        num_set = set(nums)
        max_seq = 0
        for num in nums:
            if (num + 1) not in num_set:
                max_seq = max(get_seq_len(num), max_seq)
                
        return max_seq
