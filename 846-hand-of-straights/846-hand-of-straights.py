class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        if the array isn't divisible by groupSize, there's no way you can rearrange the hands
        need a count hashmap to remember how many cards of a kind you have left to use in a run
        need a min heap to store "starting points" to determine where to start the next run of groupSize elements
        while the heap still has stuff in it:
            pop from the heap
            if the count of that card in the heap is 0: 
                continue to next loop
            iterate through "groupSize" times, incrementing the starting number
            each time you go to a new number, decrement that count in the map
            if you get a number and the count is already 0 in the map (or it's not there), you'll have a hole, so return False
        when the heap has been emptied, you made it through the entire list of nums so return True
        """
        if len(hand) % groupSize != 0:
            return False
        
        counts = { num: 0 for num in hand }
        for num in hand:
            counts[num] += 1
            
        heapq.heapify(hand) # O(n)
        while hand:
            start = heapq.heappop(hand)
            
            if start not in counts or counts[start] == 0:
                continue
                
            for card in range(start, start + groupSize):
                if card not in counts or counts[card] == 0:
                    return False
                counts[card] -= 1
                
        return True
        
        