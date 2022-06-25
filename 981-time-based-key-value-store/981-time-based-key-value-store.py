class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        need to store the key with the value
        the key can have multiple values, so it can be an array of values
        the timestamps will always be in increasing order, so if you append to the back of value array,
            the array will be in increasing order of timestamp
        """
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """
        need to find the timestamp that is less than or equal to the given timestamp
        if a timestamp like that doesn't exist (the given TS is earlier than any already set TS)
            return ""
        just loop backwards through the key's value array and return the first TS item that is <= timestamp?
        
        4
        [("", 1), ("", 3), ("", 7), ("", 8)]
                            h l m 
        """
        if key not in self.store:
            return ""
        
        # for value, ts in reversed(self.store[key]):
        #     if ts <= timestamp:
        #         return value
        
        vals = self.store[key]
        cur_max = ("", float('-inf'))
        lo, hi = 0, len(vals) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val, ts = vals[mid]
            
            if ts < timestamp:
                if ts > cur_max[1]:
                    cur_max = (val, ts)
                lo = mid + 1
            elif ts > timestamp:
                hi = mid - 1
            else:
                return val
        
        return cur_max[0]

            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)