class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        n people lined up to buy tickets - 0th person is at the front, buying their ticket.
        each index in "tickets" is a person, and the item at each index is the number of tickets they want to buy.
        person can only buy one of the tickets they want at a time, and once they buy one, they have to go to the end of line to buy more.
            if the person just bought their last ticket, then they leave the line (leave the array)
            
        you are given 'k', which is an index/person, and you need to return how long it will take them to buy all of their tickets.
        (each ticket bought (each iteration) costs 1 second)
        
        
        
        [2,3,2]
             ^
             
        can brute force it by decrementing, pop(0)ing, and pushing to back. if number is 0 after decrementing, then don't push it to the back. keep iteration counts.
            but, need to keep track of the original number.
            loop while tickets[k] != 0, and then just move the k pointer around with the person.
        """
        seconds = 0
        while tickets:
            seconds += 1
            
            tickets[0] -= 1
            if k == 0 and tickets[0] == 0:
                break
            
            front = tickets.pop(0) # remove the first guy
            k -= 1 # just shifted off, so move k to follow the person
                
            if front > 0: # if they still need to buy more...
                tickets.append(front)
                if k == -1:
                    k = len(tickets) - 1 # reset the k pointer to the back of the array if our person just went there.
            
        return seconds