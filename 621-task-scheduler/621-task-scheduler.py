class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        the answer is going to be at minimum len(tasks)
        
        does it help to find the most freq char?
        maybe the amount of different chars?
        
        use a max heap of all the counts of each char
        this way you can always take the most frequent char first and subtract from it in the heap
        each time you pop and decrement, add 1 to a time variable
        """
        counts = Counter(tasks)
        max_heap = [-counts[task] for task in counts]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()
        while max_heap or q:
            if max_heap:
                largest = -heapq.heappop(max_heap) - 1
                if largest > 0:
                    q.append((largest, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, -q.popleft()[0])
                
            time += 1
            
        return time
        
        
