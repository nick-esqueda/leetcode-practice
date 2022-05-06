class MinStack:

    def __init__(self):
        self.sta = []
        self.curr_min = float("inf")

    def push(self, val: int) -> None:
        self.sta.append(val)
        if val < self.curr_min: 
          self.curr_min = val

    def pop(self) -> None:
        oldTop = self.sta.pop()
        if self.curr_min == oldTop and oldTop not in self.sta and self.sta:
          self.curr_min = min(self.sta)
        elif not self.sta:
          self.curr_min = float("inf")
          
          
        
        """
        oldTop = 
        currMin = 46
        [47]
        
        """

    def top(self) -> int:
        return self.sta[-1]

    def getMin(self) -> int:
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()