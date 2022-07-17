class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        from 0 up to n inclusive (i), calculate how many 1's are in the binary representation of i and store that in the array at that same index
        
        can have a helper method to find how many 1's are in each int, and call it on every iteration up to n
        this will become progressively more inefficient with higher values of n since you're doing progressively more work each iteration
        
        if a num is a power of 2, then it will only have one 1
        once you move up a power of 2, the rest of the places will be what were just calculated from 0 up until the current power of 2
        add one to all of the previous calculations to get the number of ones for the curr num
        
        offset variable
        whenever you get to a new power 2, reassign offset variable
        you know you're at a new power of 2 if offset * 2 == curr num, because offset will always be a power of two
        once you get to a new power of 2, push 1 to the rtn arr, then set the offset var to be the curr power of 2
        """
        rtn = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            count = 1 + rtn[i - offset]
            rtn.append(count)
        return rtn