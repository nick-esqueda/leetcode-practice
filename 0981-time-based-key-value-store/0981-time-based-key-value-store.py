class TimeMap:

    def __init__(self):
        self.hashmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
            
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        vals = self.hashmap[key]
        for val, time in reversed(vals):
            if time <= timestamp:
                return val
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)