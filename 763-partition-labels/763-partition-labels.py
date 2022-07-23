class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        every occurance of each character within a partition needs to only be in that partition
        
        if you can know where a character's last position is, you know how long that partition would have to be at the very least
        whenever you have a new character that has a duplicate that isn't in the initial bounds of the partition, 
            you have to increase the size of the partition to be where the last occurance of that new character is
        that size might get bumped up all the way to the end of the string, but that's okay. 
        
        create a hashmap with the characters as values and index of last appearance of that char as values
        create an end variable to keep track of when the current partition would stop
        create a length variable to keep track of the size of the partition (append this to the return array whenever you cross "end")
        iterate through s
        as you come across a new character, update the end variable to be the last occurance of the current letter IF the the last occurance is farther than end
        if you are at the 'end' index, append the current size to the return array, reset the size variable
        
        worst case, will iterate through the entire string and that's it, so O(n) time, and you'll only have at most 26 letters in the map, so O(26)<1> space
        """
        
        last_indices = {}
        for i, char in enumerate(s):
            last_indices[char] = i
            
        output = []
        end = 0
        length = 0
        for i, char in enumerate(s):
            end = max(end, last_indices[char])
            length += 1
            if i == end:
                output.append(length)
                length = 0
        return output