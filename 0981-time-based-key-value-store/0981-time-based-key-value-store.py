class TimeMap:

    def __init__(self):
        self.hashmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
            
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str: # O(log(n)) TIME
        if key not in self.hashmap: 
            return ""
        
        vals = self.hashmap[key]
        val, time = self.bin_search(vals, timestamp)
        return val if time <= timestamp else ""
    
    def bin_search(self, vals, target_time):
        lo = 0
        hi = len(vals) - 1
        while lo < hi:
            mid = lo + ((hi - lo + 1) // 2) # right mid.
            val, time = vals[mid]
            
            if time <= target_time:
                lo = mid
            else:
                hi = mid - 1
        
        return vals[lo]
        
#     def get(self, key: str, timestamp: int) -> str: # O(n) TIME
#         if key not in self.hashmap:
#             return ""
        
#         vals = self.hashmap[key]
#         for val, time in reversed(vals):
#             if time <= timestamp:
#                 return val
        
#         return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)